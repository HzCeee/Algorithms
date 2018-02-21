# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        # return the sum of all node values in the subtree rooted with node
        def findTiltHelper(node):
            if not node:
                return 0
            leftSum = findTiltHelper(node.left)
            rightSum = findTiltHelper(node.right)
            self.tilt += abs(leftSum - rightSum)
            return leftSum + rightSum + node.val
        
        findTiltHelper(root)
        
        return self.tilt