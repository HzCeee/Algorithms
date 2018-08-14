class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numCount = dict()
        for num in nums:
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1
        for num, count in numCount.items():
            if count == 1:
                return num