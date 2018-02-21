# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        # return the max length from node to the leaf
        def diameterOfBinaryTreeHelper(node):
            if not node:
                return 0
            
            leftLength = diameterOfBinaryTreeHelper(node.left)
            rightLength = diameterOfBinaryTreeHelper(node.right)
            
            print('node.val: ', node.val)
            print('leftLength: ', leftLength)
            print('rightLength: ', rightLength)
            
            self.diameter = max(leftLength + rightLength + 1, self.diameter)
            
            return max(leftLength, rightLength) + 1
        
        diameterOfBinaryTreeHelper(root)
        
        return self.diameter - 1 if root else 0