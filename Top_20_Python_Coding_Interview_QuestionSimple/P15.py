# Write a program to print the following pattern.
#    *
#    * *
# -> * * *
#    * * * *
#    * * * * *

def leftpyramid():
    for i in range(0,5):
        print("\n")
        for j in range(0,i+1):
            print("*",end=' ')
leftpyramid()