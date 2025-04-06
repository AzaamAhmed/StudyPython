# This program checks if a number is positive, negative, or zero.
# It prompts the user to enter a number and then checks its value.
# If the number is less than 0, it is negative.
# If the number is greater than 0, it is positive.
# If the number is equal to 0, it is zero.
    
def check_pos_or_neg(num):
    if num < 0:
        print(f"{num} is negative")
    elif num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is zero")
        
num = int(input("Enter your wished number:"))
check_pos_or_neg(num)