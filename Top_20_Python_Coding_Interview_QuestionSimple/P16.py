# Write a program to print the following pattern.
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

def pyramid():
    k = 5-1
    for i in range(0,5):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r") # you can use print("\n") also

pyramid()