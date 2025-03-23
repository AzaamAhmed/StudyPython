# Write a program to print the following pattern.
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5

def left_number_pyramid():
    for i in range(1,5+1):
        print("\r")
        for j in range(1,i+1):
            print(j,end=' ')
left_number_pyramid()