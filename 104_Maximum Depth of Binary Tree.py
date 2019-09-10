# 104_Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS with Stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
            else:
                result = max(result, level)
        return result

# BFS with Deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return level

# One Line (Recursion)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
