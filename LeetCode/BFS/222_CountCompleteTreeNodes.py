# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeQueue = [root] if root else []
        count = 0
        while nodeQueue:
            count += len(nodeQueue)
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]
        
        return count