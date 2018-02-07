# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodeQueue = [] if not root else [root]
        result = []
        
        while nodeQueue:
            result.append(nodeQueue[-1].val)
            
            nodeQueue = [childNode for node in nodeQueue for childNode in [node.left, node.right] if childNode]
            
        return result