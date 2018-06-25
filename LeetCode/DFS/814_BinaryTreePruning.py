# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # return if the subtree rooted at node contains 1
        def pruneTreeHelper(node):
            if not node:
                return False
            
            oneInLeftTree = pruneTreeHelper(node.left)
            oneInRightTree = pruneTreeHelper(node.right)
            if oneInLeftTree or oneInRightTree:
                if not oneInLeftTree: node.left = None
                if not oneInRightTree: node.right = None
                return True
            else:
                node.left, node.right = None, None
                return True if node.val == 1 else False
            
        pruneTreeHelper(root)
        return root