# 100_Same Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

# Tuple
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def tup(t):
            return t and (t.val, tup(t.left), tup(t.right))  # right side is tuple, if 't' is None ,return None, else, return the tuple
        return tup(p) == tup(q)
