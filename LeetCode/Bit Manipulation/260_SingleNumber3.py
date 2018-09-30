from functools import reduce
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = reduce(lambda x, y: x ^ y, nums, 0) # Get the XOR of the two unique elements.
        diff &= -diff # Find the last set bit.
        res = [0, 0]
        for num in nums:
            res[num & diff == 0] ^= num
        return res
        