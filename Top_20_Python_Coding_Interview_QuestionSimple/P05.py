# Write a program to check if the given number is palindrome or not.

def checkPalindrome(num):
    temp = num
    rev = 0
    while temp>0:
        rem = temp%10
        rev = (rev*10) + rem
        temp= temp//10
    if num == rev:
        print("Is Palindrome")
    else:
        print("Not Palindrome")

num = int(input("Enter Your Number : "))
checkPalindrome(num)