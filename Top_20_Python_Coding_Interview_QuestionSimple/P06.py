# Write a program to check if the given number is Armstrong or not.

# An Armstrong number is one where the sum of its digits, each raised to the power of the number of digits, equals the number itself.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
#
# Armstrong numbers are also known as narcissistic numbers or pluperfect digital invariants.
#
# Example:  153, 370, 371, 407

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return num == sum_of_powers

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
