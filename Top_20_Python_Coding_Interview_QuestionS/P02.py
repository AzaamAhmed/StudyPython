# Write a program to find the given number is positive or negative.

def check_positive_Negative(num):
    if num<0:
        print(f"{num} is Negative")
    elif num>0:
        print(f"{num} is Positive")
    else:
        print(f"{num} is Zero")
        
num = int(input("Enter Your Number : "))
check_positive_Negative(num)
    