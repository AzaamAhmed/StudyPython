mst_pwd = input("What is the master password: ")

def view():
    try:
        with open('password.txt', 'r') as f:
            for line in f.readlines():
                # Assuming each line is stored as "name password"
                data = line.strip()
                if data:
                    name, pwd = data.split()
                    print(f"Account: {name}, Password: {pwd}")
    except FileNotFoundError:
        print("No passwords found. Please add some first.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + " " + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view), or press 'q' to quit: ").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please try again.")
