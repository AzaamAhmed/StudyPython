# Write a program to find a minimum of three numbers.
a = int(input("Enter first number  : "))
# 12
b = int(input("Enter second number : "))
# 14
c = int(input("Enter third number  : "))
# 11
smallest = 0
if a < b and a < c:
    smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c
print(smallest, "is the smallest of three numbers.")
# 11 is the smallest of three numbers.
