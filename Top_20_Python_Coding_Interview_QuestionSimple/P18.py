# Write a program to print the following pattern.
#   1
#   2  3
#   4  5  6
#   7  8  9  10
#   11 12 13 14 15

def left_num_pyramid2():
    temp = 1
    for i in range(0,6):
        print("\r")
        for j in range(1,i+1):
            print(temp,end=' ')
            temp = temp + 1
left_num_pyramid2()