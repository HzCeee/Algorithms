class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4 : 
            return False
        
        numSum = sum(nums)
        if numSum % 4 != 0: 
            return False
        
        target = [numSum / 4] * 4
        
        # return True if can form target by numbers in nums[numIndex:]
        def makesquareHelper(nums, numIndex, target):
            if numIndex == len(nums): return True
            for sideIndex in range(4):
                if target[sideIndex] >= nums[numIndex]:
                    target[sideIndex] -= nums[numIndex]
                    if makesquareHelper(nums, numIndex+1, target): 
                        return True
                    target[sideIndex] += nums[numIndex]
            return False
        
        return makesquareHelper(nums, 0, target)