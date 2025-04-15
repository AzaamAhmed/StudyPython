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

# fibbonaci sequence upto a given number of terms

def fibonacci(n):
  fib_seq = [0, 1]
  while len(fib_seq) < n:
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
  return fib_seq

num_terms = int(input("Enter the number of terms: "))
fibonacci_seq = fibonacci(num_terms)
print("Fibonacci sequence:", fibonacci_seq)


# palindrome partitioning

def partition(s: str) -> List[List[str]]:
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, path: List[str]):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


# LRU Cache implementation

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# merge intervals

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged



# implement a min heap

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def heapify(self, arr):
        self.heap = arr[:]
        for i in reversed(range(len(arr) // 2)):
            self._bubble_down(i)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)


# implement a max heap

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def heapify(self, arr):
        self.heap = arr[:]
        for i in reversed(range(len(arr) // 2)):
            self._bubble_down(i)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def _bubble_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)
            

# implement a stack using two queues

from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, val):
        self.queue1.append(val)

    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        val = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def top(self):
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        val = self.queue1.popleft()
        self.queue2.append(val)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    def is_empty(self):
        return not self.queue1
    

 # implement a Hash Table
 
class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]


# implement a Trie(Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# implement a Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# implement a Graph using adjacency list

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")


# implement Depth First Search (DFS) algorithm	& Breadth First Search (BFS) algorithm

def dfs(graph, start):
    visited = set()
    result = []

    def _dfs(v):
        if v not in visited:
            visited.add(v)
            result.append(v)
            for neighbor in graph.get(v, []):
                _dfs(neighbor)

    _dfs(start)
    return result

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

 
# Longest Substring Without Repeating Characters

def length_of_longest_substring(s: str) -> int:
    start = max_length = 0
    used_chars = {}

    for i, char in enumerate(s):
        if char in used_chars:
            start = max(start, used_chars[char] + 1)
        used_chars[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Test the function
print(length_of_longest_substring("abcabcbb"))


# same above code with different function name
# Longest Substring Without Repeating Characters    

def longest_unique_substring(s):
    char_set = set()  # To store unique characters in the window
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:  # If duplicate found, shrink the window
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])  # Add current character to the set
        max_length = max(max_length, right - left + 1)  # Update the max length
    
    return max_length

# Testing the function
print(longest_unique_substring("abcabcbb"))


# String Compression

def compress_string(s):
    compressed = []  # To store compressed parts
    count = 1  # Count of consecutive characters
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:  # If current character matches previous
            count += 1
        else:
            compressed.append(s[i-1] + str(count))  # Append character and count
            count = 1  # Reset the count
    compressed.append(s[-1] + str(count))  # Append the last character and count
    
    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string) < len(s) else s

# Testing the function
print(compress_string("aaabbccc")) 
print(compress_string("abc"))       


# find the maximum single sell profit

def buy_sell_stock_prices(stock_prices):
    current_buy = stock_prices[0]
    global_sell = stock_prices[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(stock_prices)):
        current_profit = stock_prices[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = stock_prices[i]

        if current_buy > stock_prices[i]:
            current_buy = stock_prices[i]

    return global_sell - global_profit, global_sell

stock_prices_1 = [10,9,16,17,19,23]
buy_sell_stock_prices(stock_prices_1)
# (9, 23)


stock_prices_2 = [8, 6, 5, 4, 3, 2, 1]
buy_sell_stock_prices(stock_prices_2)
# (6, 5)


# adding the inheritance

class Animal:
    def __init__(self, species: str) -> None:
        self.species = species

    def make_sound(self) -> str:
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__("Dog")
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__("Cat")
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        return f"{self.name} says Meow!"

# Usage
my_dog = Dog("Buddy", 3)
my_cat = Cat("Whiskers", 2)
print(my_dog.species)  # Output: Dog
print(my_dog.make_sound())  # Output: Buddy says Woof!
print(my_cat.species)  # Output: Cat
print(my_cat.make_sound())  # Output: Whiskers says Meow!


# Abstract Factory Pattern with Multiple Inheritance

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def create_engine(self):
        pass

class Body(ABC):
    @abstractmethod
    def create_body(self):
        pass

class LuxuryEngine(Engine):
    def create_engine(self):
        return "Luxury V8 Engine"

class SportsEngine(Engine):
    def create_engine(self):
        return "Sports Turbocharged Engine"

class LuxuryBody(Body):
    def create_body(self):
        return "Luxury Sedan Body"

class SportsBody(Body):
    def create_body(self):
        return "Sports Coupe Body"

class CarFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_body(self) -> Body:
        pass

class LuxuryCarFactory(CarFactory):
    def create_engine(self):
        return LuxuryEngine()

    def create_body(self):
        return LuxuryBody()

class SportsCarFactory(CarFactory):
    def create_engine(self):
        return SportsEngine()

    def create_body(self):
        return SportsBody()

def build_car(factory: CarFactory):
    engine = factory.create_engine()
    body = factory.create_body()
    return f"Built Car: {body.create_body()} with {engine.create_engine()}"

luxury_car = build_car(LuxuryCarFactory())
sports_car = build_car(SportsCarFactory())

print(luxury_car)
print(sports_car)


# merge intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:  # Overlapping intervals
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)
    
    return merged

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))



# next greater element

def next_greater_element(arr):
    stack = []
    nge = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            nge[index] = arr[i]
        stack.append(i)
    
    return nge

# Example usage:
arr = [4, 5, 2, 25]
print(next_greater_element(arr))


# find duplicate numbers

def find_duplicate(nums):
    # Using Floyd's Tortoise and Hare (Cycle Detection)
    slow = fast = nums[0]
    
    # Phase 1: Finding the intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Finding the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Example usage:
nums = [3, 1, 3, 4, 2]
print(find_duplicate(nums))


# Binary Search validation

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid_bst(root.left, low, root.val) and
            is_valid_bst(root.right, root.val, high))

# Example usage:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(is_valid_bst(root))


# Longest Substring Without Repeating Characters

def length_of_longest_substring(s):
    char_index = {}
    start = max_length = 0
    
    for index, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, index - start + 1)
        char_index[char] = index
    
    return max_length

# Example usage:
s = "abcabcbb"
print(length_of_longest_substring(s))

# implementing stack using queue

from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        return self.queue.popleft()
    
    def top(self):
        return self.queue[0]
    
    def empty(self):
        return not self.queue

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False



from typing import List, Self

Self.left = None
Self.right = None

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# sum of the elements 

def sum_of_elements(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

num = []
try:
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        num.append(int(input(f"Enter number {i+1}: ")))
    print("The sum of the numbers is:", sum_of_elements(num))
except ValueError:
    print("Please enter valid integers only.")
