# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodeQueue = [root] if root else []
        res = []
        while nodeQueue:
            values = [node.val for node in nodeQueue]
            res.append(sum(values) / len(values))
            
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]
        
        return res