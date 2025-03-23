# Write a program to find if the given number is prime or not.
temp = False


def checkPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                temp = True
                break
    if temp:
        print(f"{num} is not Prime")
    else:
        print(f"{num} is Prime")


num = int(input("Enter number : "))
checkPrime(num)
