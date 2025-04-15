# Write a program to find if the given number is prime or not.


def checkPrime(num):                           # Function to check if a number is prime
    if num <= 1:                               # 0 and 1 are not prime numbers
        print(f"{num} is not Prime")           # 0 and 1 are not prime numbers
        return                                 # Exit the function

    for i in range(2, num):                    # Check for factors from 2 to num-1
        if num % i == 0:                       # If num is divisible by i
            print(f"{num} is not Prime")       # num is not prime
            return                             # Exit the function
    # If no factors found, num is prime
    if num > 1:                                # Check if num is greater than 1
        for i in range(2, int(num**0.5) + 1):  # Check for factors from 2 to sqrt(num)
            if num % i == 0:                   # If num is divisible by i
                print(f"{num} is not Prime")   # num is not prime
                return                         # Exit the function
        else:                                  # If no factors found, num is prime
            print(f"{num} is Prime")           # num is prime       # num is not prime
    return                                     # Exit the function


num = int(input("Enter the Number: "))
checkPrime(num)

#OR

num = int(input("Enter a number: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):            
   print(f"{num} is Prime")                  
else:
    print(f"{num} is Not Prime")  
    print("Prime")

#OR

def is_prime(num):                             # Function to check if a number is prime
    if num <= 1:                               # 0 and 1 are not prime numbers
        return False                           # Return False for non-prime numbers
    for i in range(2, int(num**0.5) + 1):     # Check for factors from 2 to sqrt(num)
        if num % i == 0:                       # If num is divisible by i
            return False                       # Return False for non-prime numbers
    return True                                # Return True for prime numbers
num = int(input("Enter a number: "))           # Input a number to check if it's prime
if is_prime(num):                             # Check if num is prime
    print(f"{num} is Prime")                   # Print that num is prime
else:
    print(f"{num} is Not Prime")               # Print that num is not prime

