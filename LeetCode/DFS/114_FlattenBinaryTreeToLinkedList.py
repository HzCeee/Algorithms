# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        parentNode = TreeNode(None)
        nodeStack = [root]
        
        while nodeStack:
            node = nodeStack.pop()
            if not node:
                continue
            
            nodeRightBackup = node.right
            nodeLeftBackup = node.left
            
            parentNode.right = node
            parentNode = node
            parentNode.left = None
            
            nodeStack.append(nodeRightBackup)
            nodeStack.append(nodeLeftBackup)
            