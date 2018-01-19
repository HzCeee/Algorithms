class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # left denotes the index of the element after the sorted 0
        # curIndex denotes the current examined index
        # right denotes the index of the element before the sorted 2
        
        left, curIndex, right = 0, 0, len(nums) - 1
        
        while curIndex <= right:
            if nums[curIndex] == 0:
                nums[curIndex], nums[left] = nums[left], nums[curIndex]
                curIndex, left = curIndex + 1, left + 1
            elif nums[curIndex] == 1:
                curIndex += 1
            else:
                nums[curIndex], nums[right] = nums[right], nums[curIndex]
                right = right - 1