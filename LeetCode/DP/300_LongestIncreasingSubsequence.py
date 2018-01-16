class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dp[index] denotes the the length of longest increasing subsequence in nums[:index + 1]
        # dp[index] = dp[lastSmallerNumberIndex] + 1
        
        if not nums:
            return 0
        
        dp = [1 for num in nums]
        
        for index in range(1, len(nums)):
            maxDp = 0
            for i in range(index)[::-1]:
                if nums[i] < nums[index] and dp[i] > maxDp:
                    maxDp = dp[i]
            dp[index] = maxDp + 1
        
        return max(dp)
                    