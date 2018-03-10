# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right= self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                node = root.right
                while node.left:
                    node = node.left
                root.val = node.val
                root.right = self.deleteNode(root.right,root.val)
        return root