# Write a program to find the sum of two numbers.

def sumoftwo(num):
    sum = 0
    for i in num:
        sum += i
    return sum
num = []
n = int(input("Enter the Number of Elements: "))
for i in range(n):
    num.append(int(input("Enter the Number: ")))
print("The Sum of the Numbers is: ", sumoftwo(num))

