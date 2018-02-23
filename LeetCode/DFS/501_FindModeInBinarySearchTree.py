# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        valueCount = {}
        self.maxCount = 1
        def findModeHelper(node):
            if not node:
                return
            if node.val not in valueCount:
                valueCount[node.val] = 1
            else:
                valueCount[node.val] += 1
                self.maxCount = max(valueCount[node.val], self.maxCount)
            
            findModeHelper(node.left)
            findModeHelper(node.right)
        
        findModeHelper(root)
        res = [val for val in valueCount if valueCount[val] == self.maxCount]
        return res
            