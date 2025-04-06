# Write a program to find a factorial of a number.

def factorial_Loop(num):
    temp = num
    if num==0:
        print("Factorial is 1")
    elif num < 0:
        print("Factorial Not Exist")
    else:
        for i in range(1,num):
            temp = temp*i
    print(f"Factorial of {num} is {temp}")

def factorial_recursion(num):
    if num==0:
        return 1
    elif num < 0:
        print("Factorial Not Exist")
    else:
        return num*factorial_recursion(num-1)
    



num = int(input("Enter Your Number : "))
factorial_Loop(num)
print(f"Factorial of {num} is {factorial_recursion(num)}")


        