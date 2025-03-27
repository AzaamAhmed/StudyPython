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

