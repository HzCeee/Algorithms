class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []
        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            nums.append(node.val)
            inorderTraversal(node.right)
        
        inorderTraversal(root)
        
        left, right = 0, len(nums) - 1
        while left < right:
            curSum = nums[left] + nums[right]
            if curSum == k:
                return True
            if curSum < k:
                left += 1
            else:
                right -= 1
        
        return False