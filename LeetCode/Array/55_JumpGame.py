class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curIndex, maxIndex, lastIndex = 0, nums[0], len(nums) - 1
        while curIndex <= maxIndex:
            maxIndex = max(maxIndex, curIndex + nums[curIndex])
            if maxIndex >= lastIndex:
                return True
            curIndex += 1
        
        return False