# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        maxTreeDepth = [0]
        
        def maxDepthHelper(node, depth):
            if not node:
                if depth > maxTreeDepth[0]:
                    maxTreeDepth[0] = depth
                return
            maxDepthHelper(node.left, depth+1)
            maxDepthHelper(node.right, depth+1)
        
        maxDepthHelper(root, depth)
        
        return maxTreeDepth[0]