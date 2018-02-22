# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # return the constructed string rooted with node
        def tree2strHelper(node):
            if not node:
                return ""
            string = "" if not node else str(node.val)
            if node.right:
                string += '(' + tree2strHelper(node.left) + ')' + '(' + tree2strHelper(node.right) + ')'
            if node.left and not node.right:
                string += '(' + tree2strHelper(node.left) + ')'
            return string
        
        res = tree2strHelper(t)
        return res