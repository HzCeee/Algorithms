# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        subtreeSum = {}
        # return the tree sum rooted at node
        def findFrequentTreeSumHelper(node):
            if not node:
                return 0
            leftSum = findFrequentTreeSumHelper(node.left)
            rightSum = findFrequentTreeSumHelper(node.right)
            treeSum = node.val + leftSum + rightSum
            if treeSum not in subtreeSum:
                subtreeSum[treeSum] = 1
            else:
                subtreeSum[treeSum] += 1
            return treeSum
        
        findFrequentTreeSumHelper(root)
        
        maxCount = max([val for val in subtreeSum.values()])
        return [key for key in subtreeSum.keys() if subtreeSum[key] == maxCount]
            