# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = None
        
        def kthSmallestHelper(node):
            if not node or self.count == k: return
            
            kthSmallestHelper(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
            kthSmallestHelper(node.right)
        
        kthSmallestHelper(root)
        
        return self.res
        