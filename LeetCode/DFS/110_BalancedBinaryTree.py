# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        balanced = [True]
        
        def isBalancedHelper(node):
            if not balanced[0] or not node:
                return 0
            
            leftSubtreeDepth = isBalancedHelper(node.left)
            rightSubtreeDepth = isBalancedHelper(node.right)
            if abs(leftSubtreeDepth - rightSubtreeDepth) > 1:
                balanced[0] = False
                return -1
            
            return max(leftSubtreeDepth, rightSubtreeDepth) + 1
        
        isBalancedHelper(root)
        
        return balanced[0]