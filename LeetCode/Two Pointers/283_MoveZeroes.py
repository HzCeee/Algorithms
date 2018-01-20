class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # zero denotes the index of the first zero
        # nonZero denotes the index of the first non-zero element after the first zero
        
        zero = nonZero = 0
        
        while nonZero <= len(nums) - 1 and zero <= len(nums) - 1:
            nums[nonZero], nums[zero] = nums[zero], nums[nonZero]
            # find the first zero
            while zero <= len(nums) - 1 and nums[zero] != 0:
                zero += 1
            # find the first non-zero after the first zero
            nonZero = zero + 1
            while nonZero <= len(nums) - 1 and nums[nonZero] == 0:
                nonZero += 1