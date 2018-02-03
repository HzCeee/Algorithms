class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dp[num] denotes the number of possible combinations that add up to num
        # dp[num] = sum([dp[num - i] for i in nums if i <= num])
        
        dp = [1 for i in range(target + 1)]
        
        for num in range(1, len(dp)):
            dp[num] = sum([dp[num - i] for i in nums if i <= num])
        
        return dp[target]