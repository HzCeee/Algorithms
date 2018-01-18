# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        
        nodeQueue = [root]
        while nodeQueue:
            node = nodeQueue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                nodeQueue.append(node.left)
                nodeQueue.append(node.right)
        return root