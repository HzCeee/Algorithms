# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # robHelper(node) returns two elements
        # the first is the maximum money can be stoled with node as root and stole the root house
        # the second is the maximum money can be stoled with node as root but not stole the root house
        
        def robHelper(node):
            if not node:
                return (0, 0)
            left = robHelper(node.left)
            right = robHelper(node.right)
            return (left[1] + right[1] + node.val, max(left) + max(right))
        
        return max(robHelper(root))
    