# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeQueue = [root] if root else []
        result = []
        while nodeQueue:
            nodeValues = [node.val for node in nodeQueue]
            result.append(max(nodeValues))
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]
        
        return result