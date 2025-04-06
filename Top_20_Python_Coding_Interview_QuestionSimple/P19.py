# Write a program to print the following pattern.
# A
# B B
# C C C
# D D D D

def left_abc_pyramid():
    numA = 65
    for i in range(0,4):
        print("\r")
        for j in range(0,i+1):
            temp = chr(numA)
            print(temp,end=' ')
        numA = numA + 1
left_abc_pyramid()