# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        return a list of root node whose value falls in the range [start, end]
        def generateTreesHelper(start, end):
            res = []
            for rootVal in range(start, end+1):
                root = TreeNode(rootVal)
                for leftNode in generateTreesHelper(start, rootVal-1):
                    for rightNode in generateTreesHelper(rootVal+1, end):
                        root.left, root.right = leftNode, rightNode
                        res.append(root)
            return res if res else [None]
        return generateTreesHelper(1, n)
                    
            
            