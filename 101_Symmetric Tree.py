#101_Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L,R):
            if L and R and L.val==R.val:
                return isSym(L.left,R.right) and isSym(L.right,R.left)
            return L==R
        return isSym(root,root)