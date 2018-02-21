# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.curGreaterValue = 0
        def convertBST(node):
            if not node:
                return
            convertBST(node.right)
            self.curGreaterValue += node.val
            node.val = self.curGreaterValue
            convertBST(node.left)
            
        convertBST(root)
        return root
            