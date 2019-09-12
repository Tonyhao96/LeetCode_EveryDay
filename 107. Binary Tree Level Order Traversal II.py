#107_Binary Tree Level Order Traversal II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root: return []
        queue, nodes = [root], []
        while queue:
            nodes.append([q.val for q in queue])
            queue = [q for node in queue for q in (node.left, node.right) if q]
        nodes.reverse()
        return nodes