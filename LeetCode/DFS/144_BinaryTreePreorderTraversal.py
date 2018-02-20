# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeStack = [root] if root else []
        result = []
        while nodeStack:
            node = nodeStack.pop()
            if not node:
                continue
            result.append(node.val)
            nodeStack.append(node.right)
            nodeStack.append(node.left)
        
        return result