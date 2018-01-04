# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        exist = [False]
        
        def hasPathSumHelper(node, curSum):
            if not node:
                return
            
            if not node.left and not node.right:
                if curSum + node.val == sum:
                    exist[0] = True
                    return
            
            hasPathSumHelper(node.left, curSum + node.val)
            hasPathSumHelper(node.right, curSum + node.val)
        
        hasPathSumHelper(root, 0)
        
        return exist[0]