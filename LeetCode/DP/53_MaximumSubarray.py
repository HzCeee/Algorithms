class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # DP[index] denotes the maximum sum consisting of nums[index] in subarray nums[:index+1]
        # if DP[index - 1] + nums[index] > nums[index]: DP[index] = DP[index - 1] + nums[index] 
        # else: DP[index] = nums[index]
        
        minValue = -float("inf")
        dp = [minValue for i in range(len(nums))]
        dp[0] = nums[0]
        maximumSubarraySum = dp[0]
        
        for index in range(1, len(dp)):
            if dp[index - 1] + nums[index] > nums[index]:
                dp[index] = dp[index - 1] + nums[index]
            else:
                dp[index] = nums[index]
                
            maximumSubarraySum = max(maximumSubarraySum, dp[index])
        
        return maximumSubarraySum