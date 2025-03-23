# Write a program to find a fibonacci of a number.

def fibonacciSeries(num):
    a = 0
    b = 1
    for i in range(0,num):
        print(a)
        sum = a+b
        a = b
        b = sum

num = int(input("Enter Number of Term : "))
fibonacciSeries(num)