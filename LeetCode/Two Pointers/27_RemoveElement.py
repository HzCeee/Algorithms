class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # newIndex denotes the index of unchecked position in the new array
        # curIndex denotes the index of current examined number
        
        newIndex, newLength = 0, 0
        for curIndex in range(len(nums)):
            if nums[curIndex] != val:
                nums[newIndex] = nums[curIndex]
                newIndex, newLength = newIndex + 1, newLength + 1
            else:
                continue
        
        return newLength