class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dpMax[index] denotes the maximum product consisting of nums[index] in subarray nums[:index+1]
        # dpMin[index] denotes the minimum product consisting of nums[index] in subarray nums[:index+1]
        # dpMax[index] = max(dpMax[index - 1] * nums[index], dpMin[index - 1] * nums[index], nums[index])
        # dpMin[index] = min(dpMax[index - 1] * nums[index], dpMin[index - 1] * nums[index], nums[index])
        
        dpMax = [1 for num in nums]
        dpMin = [1 for num in nums]
        dpMax[0] = dpMin[0] = nums[0]
        
        for index in range(1, len(nums)):
            num1 = dpMax[index - 1] * nums[index]
            num2 = dpMin[index - 1] * nums[index]
            num3 = nums[index]
            dpMax[index] = max(num1, num2, num3)
            dpMin[index] = min(num1, num2, num3)
        
        return max(dpMax)