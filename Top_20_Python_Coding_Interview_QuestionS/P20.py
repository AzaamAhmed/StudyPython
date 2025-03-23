# Write a program to print the following pattern.
# A
# B C
# D E F
# G H I J

def left_abc_pyramid2():
    numA = 65
    for i in range(0,4):
        print("\r")
        for j in range(0,i+1):
            temp = chr(numA)
            print(temp,end=' ')
            numA = numA + 1
left_abc_pyramid2()