# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        nodeList = []
        
        def pathSumHelper(node, curNodeList): # return 
            if not node:
                return
            
            if not node.left and not node.right and sum(curNodeList) + node.val == target:
                curNodeList.append(node.val)
                result.append(curNodeList)
                return
            if node.left:
                pathSumHelper(node.left, curNodeList + [node.val])
            if node.right:
                pathSumHelper(node.right, curNodeList + [node.val])
        
        pathSumHelper(root, nodeList)
        
        return result    
                