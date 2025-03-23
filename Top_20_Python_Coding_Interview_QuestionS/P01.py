# Write a program to print the given number is odd or even.

def odd_even_checker(num):
    if num % 2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

num = int(input("Enter Your Number : "))
odd_even_checker(num)
    
