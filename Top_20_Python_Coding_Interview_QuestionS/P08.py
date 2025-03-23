# Write a program to find a maximum of two numbers.
def maximum(a, b):

    if a >= b:
        return a
    else:
        return b


a = int(input("Enter a number: "))
# input1: 2
b = int(input("Enter a number: "))
# input2: 4
print(maximum(a, b))
# output: 4
