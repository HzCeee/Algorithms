class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # left denotes the index of the most left number in the contiguous subarray
        
        if not nums:
            return 0
        
        subarraySum = 0
        left = 0
        exist = False
        minLength = float('inf')
        
        for index in range(len(nums)):
            subarraySum += nums[index]
            while subarraySum >= s:
                exist = True
                minLength = min(minLength, index - left + 1)
                subarraySum -= nums[left]
                left += 1
        
        return minLength if exist else 0