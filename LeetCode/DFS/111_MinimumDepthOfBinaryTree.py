# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        depth = 1
        minTreeDepth = [float("inf")]
        
        def minDepthHelper(node, depth):
            if not node:
                return
            
            if not node.left and not node.right:
                if depth <= minTreeDepth[0]:
                    minTreeDepth[0] = depth
                    return
            
            minDepthHelper(node.left, depth+1)
            minDepthHelper(node.right, depth+1)
        
        minDepthHelper(root, depth)
        
        return minTreeDepth[0]