# Write a program to find a maximum of three numbers.
def maximum(a, b, c):

    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
        
    return largest


a = int(input("Enter a number: "))
# Input1: 10
b = int(input("Enter a number: "))
# Input2: 14
c = int(input("Enter a number: "))
# Input3: 12
print(maximum(a, b, c))
# Output: 14