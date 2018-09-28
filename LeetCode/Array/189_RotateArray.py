class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rotateCount = k % len(nums)
        
        for cnt in range(rotateCount):
            value = nums[0]
            for index in range(len(nums)):
                toPtr = (index + 1) % len(nums)
                tmp = nums[toPtr]
                nums[toPtr] = value
                value = tmp