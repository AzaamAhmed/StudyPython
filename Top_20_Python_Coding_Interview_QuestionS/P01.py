# Write a program to print the given number is odd or even.
 
# 1st we want to check whether its odd or even by iusing the modulus operator 
# its give the remainder of the devision
# and if its 0 then its even otherwise its odd

def odd_even_checker(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

num = int(input("Enter the Number: "))
odd_even_checker(num)