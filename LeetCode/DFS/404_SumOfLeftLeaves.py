# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeStack = [(root, 'root')] if root else []
        sumLeft = 0
        while nodeStack:
            node, nodeType = nodeStack.pop()
            if not node.left and not node.right and nodeType == 'left':
                sumLeft += node.val
            if node.left:
                nodeStack.append((node.left, 'left'))
            if node.right:
                nodeStack.append((node.right, 'right'))
        
        return sumLeft