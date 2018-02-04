class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[num] denotes whether num can be the summation of subarray in nums
        # dp[num] = any(dp[num - i] for i in nums if i<= num)
        # dp[num] = dp[num] or dp[num - nums[i]]
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = [False for num in range(target + 1)]
        dp[0] = True
        
        # idea: whether choose i to form the summation of num
        # if choose i, dp[num] = dp[num - nums[i]]
        # if not choose i, dp[num] = dp[num]
        for i in range(len(nums)):
            for num in range(nums[i], target + 1)[::-1]: # reverse so that dp[num] only depends on dp[num] and dp[num - nums[i]]
                 dp[num] = dp[num] or dp[num - nums[i]]
                
        return dp[target]
        