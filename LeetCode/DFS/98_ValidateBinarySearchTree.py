# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        isValid = [True]
        
        maximumThreshold = float("inf")
        minimumThreshold = - float("inf")
        
        def isValidHelper(node, minimumThreshold, maximumThreshold):
            if not node or not isValid[0]:
                return
            if node.val >= maximumThreshold or node.val <= minimumThreshold:
                isValid[0] = False
                return
            isValidHelper(node.left, minimumThreshold, node.val)
            isValidHelper(node.right, node.val, maximumThreshold)
        
        isValidHelper(root, minimumThreshold, maximumThreshold)
        return isValid[0]