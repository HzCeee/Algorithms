class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # dp[index] denotes the largest number of subset including nums[index] as the largest number
        # dp[index] = max([dp[i] + 1 for i in range(index) if nums[index] % nums[i] == 0])
        if not nums:
            return []
        
        dp = [1 for i in range(len(nums))]
        maxIndex = 0
        nums.sort()
        
        # dp
        for index in range(1, len(nums)):
            dp[index] = max([dp[i] + 1 if nums[index] % nums[i] == 0 else 1 for i in range(index)])
            if dp[index] > dp[maxIndex]: maxIndex = index
        
        # reconstruct
        ans = []
        curNumber = nums[maxIndex]
        curDp = dp[maxIndex]
        for index in range(maxIndex + 1)[::-1]:
            if dp[index] == curDp and curNumber % nums[index] == 0:
                ans.append(nums[index])
                curDp -= 1
                
        return ans