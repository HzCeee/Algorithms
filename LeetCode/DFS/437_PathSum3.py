# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.possibleSum = []
        self.count = 0
        # return a list refering to the possible sum including node.val
        def pathSumHelper(node):
            if not node:
                return []
            
            leftSum = pathSumHelper(node.left)
            rightSum = pathSumHelper(node.right)
            
            nodeSum = [node.val]
            if node.val == target: self.count += 1
            for value in leftSum + rightSum:
                if node.val + value == target: self.count += 1
                nodeSum.append(value + node.val)
                
            self.possibleSum += nodeSum
            return nodeSum
        
        pathSumHelper(root)
        return self.count