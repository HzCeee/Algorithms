# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        nodeQueue = [root]
        
        while nodeQueue:
            values = [node.val if node else None for node in nodeQueue]
            if values != values[::-1]:
                return False
            
            nodeQueue = [childNode for node in nodeQueue if node for childNode in [node.left, node.right]]
        
        return True
            
            