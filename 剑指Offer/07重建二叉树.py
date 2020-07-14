#面试题07.重建二叉树

#Using Recursive Method
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
            root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
            return root
        else:
            return None

#Using Iteration Method
#Time complexity: O(n)  Space complexity: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        stack, idx = [], 0
        stack.append(root)
        
        for i in range(1, len(preorder)):
            if inorder[idx] == stack[-1].val:
                while stack and stack[-1].val == inorder[idx]:
                    node = stack[-1]
                    stack.pop()
                    idx += 1
                node.right = TreeNode(preorder[i])
                stack.append(node.right)
            else:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
        return root