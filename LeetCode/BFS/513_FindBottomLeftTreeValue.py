# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeQueue = [root] if root else []
        bottomLeftValue = None
        while nodeQueue:
            nodeValue = [node.val for node in nodeQueue]
            bottomLeftValue = nodeValue[0]
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]
        
        return bottomLeftValue