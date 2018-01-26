class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # firstPtr denotes the index of the first number
        # secondPtr denotes the index of the second number
        
        firstPtr, secondPtr = 0, 1
        count = 0
        
        nums.sort()
        
        while firstPtr < len(nums) and secondPtr < len(nums):
            currentFirstNumber = nums[firstPtr]
            currentsecondNumber = nums[secondPtr]
            
            if nums[secondPtr] - nums[firstPtr] >= k:
                if nums[secondPtr] - nums[firstPtr] == k: count += 1
                while firstPtr < len(nums) and nums[firstPtr] <= currentFirstNumber:
                    firstPtr += 1
                secondPtr = firstPtr + 1
            else:
                while secondPtr < len(nums) and nums[secondPtr] <= currentsecondNumber:
                    secondPtr += 1
        
        return count