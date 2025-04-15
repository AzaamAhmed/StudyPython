# Write a program to check if the given number is palindrome or not.

num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#OR
def is_palindrome(num):
    return str(num) == str(num)[::-1]
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
    
