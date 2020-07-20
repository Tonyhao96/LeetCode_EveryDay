#590_N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#Recursion
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def recur(root):
            if not root: return None
            children = root.children
            for i in children:
                recur(i)
            res.append(root.val)
        recur(root)
        return res

#Iteration
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return None
        stack, res =[root,], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in node.children:
                stack.append(i)
        return res[::-1]