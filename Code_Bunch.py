"""	
This is a collection of Python code snippets for beginner & Advanced Python codes.
I will comment it after I finish the code by myself.

"""	


#finding the calculate of the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(6))

#counting the upper case

def count_upper_case(s):
    return sum(1 for char in s if char.isupper())

print(count_upper_case("Hello World I am a Python Developer Welcome to the World of Python"))

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))


# Flatten a nested list
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1, [2, [3, 4], 5], 6])) 

# Finding the maximum number in a list

def max_num(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

# Finding the minimum number in a list	

def min_num(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min


#program to check if a binary tree is balanced

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    if not root:
        return True

    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    return abs(height(root.left) - height(root.right)) <= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(is_balanced(root)) 

#program to find the maximum subarray sum

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#program to find the longest common prefix

def longest_common_prefix(strs):
    if not strs:
        return ""
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    return min(strs)

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["ab", "a"]))


# program to find the intersection of two sets

def intersection(set1, set2):
    return set1 & set2

print(intersection({1, 2, 3}, {2, 3, 4}))


# program to find the union of two sets

def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(5, 3, 'add'))

# convert celsius to fahrenheit 

def celsius_to_fahrenheit(temps):
    return [(temp * 9/5) + 32 for temp in temps]
print(celsius_to_fahrenheit([0, 20, 37]))


# implement a queue using collection.queue

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())

# program to check if a string is a palindrome

def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
    
# program to find the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")


# program to find the largest number in a list

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [10, 5, 8, 20, 3]
largest_num = find_largest(nums)
print(f"The largest number is {largest_num}")


# program to reverse a string.

def reverse_string(string):
    return string[::-1]

text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)


# program to find the frequency of numbers in a list

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)

# program to check if a number is prime

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")




# program to find the common elements between two lists

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(common)


# Python program to sort a list of elements using the bubble sort algorithm.

def bubble_sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]

nums = [5, 2, 8, 1, 9]
bubble_sort(nums)
print(nums)


# program to remove duplicates from a list

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)