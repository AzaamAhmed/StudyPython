# Binary Search Tree (BST) Insertion

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Example usage:
# Constructing the following BST:
#     4
#    / \
#   2   7
#  / \
# 1   3

root = TreeNode(4)
insert_into_bst(root, 2)
insert_into_bst(root, 7)
insert_into_bst(root, 1)
insert_into_bst(root, 3)


# Combination Sum

def combination_sum(candidates, target):
    result = []
    candidates.sort()
    find_combinations(candidates, target, 0, [], result)
    return result

def find_combinations(candidates, target, index, path, result):
    if target == 0:
        result.append(path)
        return
    for i in range(index, len(candidates)):
        if candidates[i] > target:
            break
        find_combinations(candidates, target - candidates[i], i, path + [candidates[i]], result)

# Example usage:
candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates, target))  # Output: [[2,2,3],[7]]



# Binary Tree Level Order Traversal

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

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

# Example usage:
# Constructing the following binary tree:
#     3
#    / \
#   9  20
#      / \
#     15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order_traversal(root))  # Output: [[3],[9,20],[15,7]]


# Course Schedule (Detecting Cycles in a Directed Graph)

from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    in_degree = [0] * numCourses
    adjacency_list = defaultdict(list)
    for dest, src in prerequisites:
        adjacency_list[src].append(dest)
        in_degree[dest] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adjacency_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return visited == numCourses

# Example usage:
numCourses = 2
prerequisites = [[1,0]]
print(can_finish(numCourses, prerequisites))  # Output: True



# Evaluate Reverse Polish Notation 

def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:  # token == "/"
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))
    return stack[0]

# Example usage:
tokens = ["2", "1", "+", "3", "*"]
print(eval_rpn(tokens))  # Output: 9



# Longest Increasing Subsequence	

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example usage:
nums = [10,9,2,5,3,7,101,18]
print(length_of_lis(nums))  # Output: 4


# Serialize and Deserialize Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                vals.append("#")
            else:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        vals = iter(data.split())
        return helper()

# Example usage:
# Constructing the following tree:
#     1
#    / \
#   2   3
#      / \
#     4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
data = codec.serialize(root)
print(data)  # Output: "1 2 # # 3 4 # # 5 # #"
new_root = codec.deserialize(data)
print(codec.serialize(new_root) == data)  # Output: True    


# Maximum Subarray

def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6


# median of two sorted arrays

def findMedianSortedArrays(nums1, nums2):
    def kthElement(arr1, arr2, k):
        if not arr1:
            return arr2[k]
        if not arr2:
            return arr1[k]
        idx1, idx2 = len(arr1) // 2, len(arr2) // 2
        median1, median2 = arr1[idx1], arr2[idx2]
        if idx1 + idx2 < k:
            if median1 > median2:
                return kthElement(arr1, arr2[idx2 + 1:], k - idx2 - 1)
            else:
                return kthElement(arr1[idx1 + 1:], arr2, k - idx1 - 1)
        else:
            if median1 > median2:
                return kthElement(arr1[:idx1], arr2, k)
            else:
                return kthElement(arr1, arr2[:idx2], k)

    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 1:
        return kthElement(nums1, nums2, total_len // 2)
    else:
        return (kthElement(nums1, nums2, total_len // 2 - 1) +
                kthElement(nums1, nums2, total_len // 2)) / 2.0

# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

# Trapping Rain Water

def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water

# Example usage:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6


# N-Queens Problem (Backtracking) 

def solveNQueens(n):
    def backtrack(row, diagonals, anti_diagonals, cols, state):
        if row == n:
            board.append(["".join(row) for row in state])
            return
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col
            if (col in cols or curr_diag in diagonals or
                    curr_anti_diag in anti_diagonals):
                continue
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            state[row][col] = 'Q'
            backtrack(row + 1, diagonals, anti_diagonals, cols, state)
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
            state[row][col] = '.'

    board = []
    empty_board = [['.'] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return board

# Example usage:
n = 4
for solution in solveNQueens(n):
    for row in solution:
        print(row)
    print()
