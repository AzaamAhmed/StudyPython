from flask import Flask, request, jsonify, session # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
from cryptography.fernet import Fernet # type: ignore
import sqlite3
import re, os, time
from flask_limiter import Limiter # type: ignore
from flask_limiter.util import get_remote_address # type: ignore

# Generate encryption key (store securely)
if not os.path.exists("key.key"):
    with open("key.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

encryption_key = load_key()
cipher_suite = Fernet(encryption_key)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])  # Brute-force protection

# Database setup
def init_db():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY, 
                        username TEXT UNIQUE, 
                        password_hash TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY, 
                        user_id INTEGER, 
                        site TEXT, 
                        encrypted_password TEXT, 
                        FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

init_db()

# Password Validation
def validate_password(password):
    if len(password) < 12:
        return "Password must be at least 12 characters long"
    if not re.search("[A-Z]", password):
        return "Password must contain an uppercase letter"
    if not re.search("[a-z]", password):
        return "Password must contain a lowercase letter"
    if not re.search("[0-9]", password):
        return "Password must contain a number"
    if not re.search("[@$!%*?&]", password):
        return "Password must contain a special character"
    return None

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]
    
    validation_error = validate_password(password)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    
    password_hash = generate_password_hash(password)
    
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400
    finally:
        conn.close()
    
    return jsonify({"message": "User registered successfully"})

@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    
    if not user or not check_password_hash(user[1], password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    session["user_id"] = user[0]
    session["last_active"] = time.time()
    return jsonify({"message": "Login successful"})

@app.route("/store", methods=["POST"])
def store_password():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    site = data["site"]
    password = data["password"]
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()
    
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (user_id, site, encrypted_password) VALUES (?, ?, ?)", (session["user_id"], site, encrypted_password))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Password stored securely"})

@app.route("/retrieve", methods=["GET"])
def retrieve_passwords():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute("SELECT site, encrypted_password FROM passwords WHERE user_id = ?", (session["user_id"],))
    records = cursor.fetchall()
    conn.close()
    
    passwords = [{"site": r[0], "password": cipher_suite.decrypt(r[1].encode()).decode()} for r in records]
    return jsonify({"passwords": passwords})

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"})

if __name__ == "__main__":
    app.run(debug=True)
