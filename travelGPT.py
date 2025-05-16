print("Welcome to the TravelGPT 3.0. Lets plan an adventure")
try:
    enter = int(input("1 - Start, 2 - quit: "))
except ValueError:
    print("Invalid input. Exiting.")
    enter = 2

while enter == 1:
    destination = input("Do you have a destination in mind : ").lower()
    if destination == "yes":
        print("let's get started")
        transport = input("How do you want to travel? (car, bus, train, plane) : ").lower()
        if transport == "plane":
            class_type = input("What class do you want to fly? (economy, business, first) : ").lower()
            if class_type == "economy":
                print("You have chosen economy class. Enjoy your flight!")
            elif class_type == "business":
                print("You have chosen business class. Enjoy your flight!")
            elif class_type == "first":
                print("You have chosen first class. Enjoy your flight!")
            else:
                print("Invalid class type. Please choose economy, business, or first.")
        elif transport == "train":
            class_type = input("What class do you want to travel? (sleeper, AC, general) : ").lower()
            if class_type == "sleeper":
                print("You have chosen sleeper class. Enjoy your journey!")
            elif class_type == "ac":
                print("You have chosen AC class. Enjoy your journey!")
            elif class_type == "general":
                print("You have chosen general class. Enjoy your journey!")
            else:
                print("Invalid class type. Please choose sleeper, AC, or general.")
        elif transport == "car":
            print("You have chosen to travel by car. Enjoy your road trip!")
        elif transport == "bus":
            print("You have chosen to travel by bus. Enjoy your journey!")
        else:
            print("Invalid transport mode. Please choose car, bus, train, or plane.")
    elif destination == "no":
        print("No worries! Maybe next time.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    try:
        enter = int(input("1 - Start, 2 - quit: "))
    except ValueError:
        print("Invalid input. Exiting.")
        enter = 2

print("Thank you for using TravelGPT 3.0. Have a great day!")