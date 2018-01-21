class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[index] denotes the maximum amount of money consisting money nums[index]
        # dp[index] = nums[index] + max(dp[index - 2], dp[index - 3])
        
        if len(nums) == 1:
            return nums[0]
        
        # include nums[0]
        dp = [0 for i in range(len(nums) + 3)]
        for index in range(3, len(dp)):
            dp[index] = nums[index - 3] + max(dp[index - 2], dp[index - 3])
        
        max1 = max(dp[-3:-1])
        
        # exclude nums[0]
        dp = [0 for i in range(len(nums) + 3)]
        for index in range(4, len(dp)):
            dp[index] = nums[index - 3] + max(dp[index - 2], dp[index - 3])
        
        max2 = max(dp[-2:])
        
        return max(max1, max2)