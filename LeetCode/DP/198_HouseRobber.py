class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dp[index] denotes the maximum amount of money consisting money nums[index]
        # dp[index] = nums[index] + max(dp[index - 2], dp[index - 3])
        
        dp = [0 for i in range(len(nums) + 3)]
        
        for index in range(3, len(dp)):
            dp[index] = nums[index - 3] + max(dp[index - 2], dp[index - 3])
        
        return max(dp[-2:])