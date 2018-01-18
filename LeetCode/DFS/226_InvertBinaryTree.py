# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invertTreeHelper(node):
            if not node:
                return
            
            node.left, node.right = node.right, node.left
            
            invertTreeHelper(node.left)
            invertTreeHelper(node.right)
        
        invertTreeHelper(root)
        return root

    def invertTree_stack(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        
        nodeStack = [root]
        while nodeStack:
            node = nodeStack.pop()
            
            node.left, node.right = node.right, node.left
            
            if node.left: nodeStack.append(node.left)
            if node.right: nodeStack.append(node.right)
        
        return root