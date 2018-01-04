# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        symmetric = [True]
        
        def isSymmetricHelper(node1, node2):
            if not node1 and not node2:
                return
            if not node1 or not node2 or node1.val != node2.val:
                symmetric[0] = False
                return
            isSymmetricHelper(node1.left, node2.right)
            isSymmetricHelper(node1.right, node2.left)
        
        if root:
            isSymmetricHelper(root.left, root.right)
        
        return symmetric[0]