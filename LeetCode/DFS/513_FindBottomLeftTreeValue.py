# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth, maximumDepth = 0, -1
        nodeStack = [[root, depth]] if root else []
        bottomLeftValue = None
        while nodeStack:
            node, depth = nodeStack.pop()
            if depth > maximumDepth:
                bottomLeftValue = node.val
                maximumDepth = depth
            
            if node.right: nodeStack.append([node.right, depth + 1])
            if node.left: nodeStack.append([node.left, depth + 1])
            
        return bottomLeftValue
            