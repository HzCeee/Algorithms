# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        
        medianIndex = len(nums) // 2
        node = TreeNode(nums[medianIndex])
        
        node.left = self.sortedArrayToBST(nums[:medianIndex])
        node.right = self.sortedArrayToBST(nums[medianIndex+1:])
        
        return node