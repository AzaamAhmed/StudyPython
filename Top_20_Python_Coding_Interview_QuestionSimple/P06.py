# Write a program to check if the given number is Armstrong or not.
num = int(input("Enter a number: "))
# Input: 407
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# Output: 407 is an Armstrong number