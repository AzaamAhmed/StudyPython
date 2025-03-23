import os
import base64
import getpass
import json
import hashlib
from cryptography.fernet import Fernet
from pathlib import Path

# Secure Storage Paths
MASTER_PASSWORD_FILE = Path("master_pwd.json")
PASSWORD_STORAGE_FILE = Path("passwords.json")
KEY_FILE = Path("encryption.key")

# Strong Iteration Count for Hashing
HASH_ITERATIONS = 200_000


def generate_key():
    """Generates a strong encryption key and securely stores it."""
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def load_encryption():
    """Loads encryption mechanism using AES-256 (Fernet)."""
    key = generate_key()
    return Fernet(key)


cipher = load_encryption()


def hash_password(password: str, salt: bytes = None):
    """Hashes password using PBKDF2-HMAC-SHA256 with a salt."""
    if salt is None:
        salt = os.urandom(16)  # 16-byte salt

    hashed_pwd = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, HASH_ITERATIONS
    )
    return base64.b64encode(salt + hashed_pwd).decode()


def verify_password(input_password: str, stored_hash: str):
    """Verifies if input password matches stored hashed password."""
    decoded_data = base64.b64decode(stored_hash.encode())
    salt = decoded_data[:16]
    stored_hashed_pwd = decoded_data[16:]

    input_hashed_pwd = hashlib.pbkdf2_hmac(
        "sha256", input_password.encode(), salt, HASH_ITERATIONS
    )

    return input_hashed_pwd == stored_hashed_pwd


def initialize_master_password():
    """Sets up or verifies master password securely."""
    if MASTER_PASSWORD_FILE.exists():
        with open(MASTER_PASSWORD_FILE, "r") as file:
            stored_hash = json.load(file).get("master_password")

        for _ in range(3):  # Allow 3 attempts
            entered_pwd = getpass.getpass("Enter Master Password: ")
            if verify_password(entered_pwd, stored_hash):
                print("✅ Access Granted")
                return True
            else:
                print("❌ Incorrect Password")
        print("🔴 Too many failed attempts. Exiting.")
        exit(1)

    else:
        print("🔒 Setting up a new master password...")
        while True:
            new_pwd = getpass.getpass("Create a Master Password: ")
            confirm_pwd = getpass.getpass("Confirm Password: ")
            if new_pwd == confirm_pwd and len(new_pwd) >= 8:
                hashed_master_pwd = hash_password(new_pwd)
                with open(MASTER_PASSWORD_FILE, "w") as file:
                    json.dump({"master_password": hashed_master_pwd}, file)
                print("✅ Master Password Set")
                return True
            else:
                print("❌ Passwords must match & be at least 8 characters")


def load_passwords():
    """Loads and decrypts stored passwords."""
    if PASSWORD_STORAGE_FILE.exists():
        with open(PASSWORD_STORAGE_FILE, "r") as file:
            try:
                encrypted_data = file.read().encode()
                if encrypted_data:
                    decrypted_data = cipher.decrypt(encrypted_data).decode()
                    return json.loads(decrypted_data)
            except Exception:
                print("⚠️ Failed to decrypt data. Possible corruption.")
                return {}
    return {}


def save_passwords(passwords):
    """Encrypts and securely stores passwords."""
    encrypted_data = cipher.encrypt(json.dumps(passwords).encode())
    with open(PASSWORD_STORAGE_FILE, "wb") as file:
        file.write(encrypted_data)


def add_password():
    """Adds a new account & encrypted password to storage."""
    passwords = load_passwords()

    account = input("Enter Account Name: ").strip()
    if account in passwords:
        print("⚠️ Account already exists. Use update instead.")
        return

    password = getpass.getpass("Enter Password: ")
    passwords[account] = password
    save_passwords(passwords)
    print("✅ Password Added Securely")


def view_passwords():
    """Displays stored accounts securely."""
    passwords = load_passwords()
    if not passwords:
        print("⚠️ No passwords stored.")
        return

    print("\n🔐 Stored Accounts:")
    for account in passwords.keys():
        print(f"- {account}")


def retrieve_password():
    """Retrieves & decrypts a specific account password."""
    passwords = load_passwords()
    account = input("Enter Account Name to Retrieve: ").strip()

    if account in passwords:
        print(f"🔑 Password for {account}: {passwords[account]}")
    else:
        print("⚠️ Account not found.")


def delete_password():
    """Deletes a specific account password."""
    passwords = load_passwords()
    account = input("Enter Account Name to Delete: ").strip()

    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print("✅ Password Deleted Securely")
    else:
        print("⚠️ Account not found.")


def main():
    """Main function to run the password manager."""
    initialize_master_password()

    while True:
        print("\n🔹 Password Manager Menu:")
        print("1. Add Password")
        print("2. View Stored Accounts")
        print("3. Retrieve Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            retrieve_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("🔒 Exiting Securely.")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
