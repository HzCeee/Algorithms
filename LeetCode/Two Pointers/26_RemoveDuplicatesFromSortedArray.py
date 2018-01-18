class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # newIndex denotes the index of unchecked position in the new array
        # curIndex denotes the index of current examined number
        
        if not nums:
            return 0
        
        newIndex = 1
        newLength = 1
        for curIndex in range(1, len(nums)):
            if nums[curIndex] == nums[newIndex - 1]:
                continue
            else:
                nums[newIndex] = nums[curIndex]
                newIndex += 1
                newLength += 1
                
        return newLength