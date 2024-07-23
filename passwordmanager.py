pwd = input("What is the master passwrod : ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to add a new password or view existing ones : ")
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
       print("Invalid Mode...!") 
       continue