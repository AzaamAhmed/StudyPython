# Write a program to find a minimum of two numbers.
def minimum(a, b):

    if a <= b:
        return a
    else:
        return b


a = int(input("Enter a number: "))
# input1: 2
b = int(input("Enter a number: "))
# input2: 4
print(minimum(a, b))
# output: 2
