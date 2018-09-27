class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newNums = [float("-inf")] + nums + [float("-inf")]
        for index in range(1, len(newNums) - 1):
            if newNums[index] > newNums[index - 1] and newNums[index] > newNums[index + 1]:
                return index - 1