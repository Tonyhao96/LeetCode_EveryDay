#110_Balanced Binary Tree
class Solution(object):
    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1

        
    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1 : return -1     #When the subtree is unbalanced, the return of -1 is forced in the exact statement but just in a deeper call.
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1