# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        depth = 0
        treePaths = []
        
        def binaryTreePathsHelper(node, prevPath, depth):
            if not node:
                return
            
            if depth != 0:
                curPath = str(prevPath) + "->" + str(node.val)
            else:
                curPath = prevPath + str(node.val)
            
            if not node.left and not node.right:
                treePaths.append(curPath)
                return
            
            binaryTreePathsHelper(node.left, curPath, depth+1)
            binaryTreePathsHelper(node.right, curPath, depth+1)
        
        binaryTreePathsHelper(root, "", depth)
        
        return treePaths