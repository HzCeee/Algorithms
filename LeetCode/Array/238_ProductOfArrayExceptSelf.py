class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftProd, rightProd = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))]
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            leftProd[i] *= prod
            
        prod = 1
        for i in range(len(nums) - 1)[::-1]:
            prod *= nums[i + 1]
            rightProd[i] *= prod
        
        output = []
        for i in range(len(nums)):
            output.append(leftProd[i]*rightProd[i])
        return output
        