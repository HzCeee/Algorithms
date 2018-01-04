# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        isSame = [True]
        
        def isSameTreeHelper(node1, node2):
            if not node1 and not node2:
                return
            if not node1 or not node2 or node1.val != node2.val:
                isSame[0] = False
                return
            
            isSameTreeHelper(node1.left, node2.left)
            isSameTreeHelper(node1.right, node2.right)
        
        isSameTreeHelper(p, q)
        
        return isSame[0]