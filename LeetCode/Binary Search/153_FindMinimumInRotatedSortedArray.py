class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        midPtr = len(nums) // 2
        firstPart, secondPart = nums[:midPtr], nums[midPtr:]
        if firstPart[-1] - firstPart[0] >= 0 and secondPart[-1] - secondPart[0] >= 0:
            return secondPart[0] if firstPart[0] > secondPart[0] else firstPart[0]
        elif secondPart[-1] - secondPart[0] < 0:
            return self.findMin(secondPart)
        else:
            return self.findMin(firstPart)