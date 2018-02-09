import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.numsDict = {num: [] for num in nums}
        for index, num in enumerate(nums):
            self.numsDict[num].append(index)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = None
        for curRandomNumber in range(len(self.numsDict[target])):
            if random.randint(0, curRandomNumber) == 0:
                result = self.numsDict[target][curRandomNumber]
        
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)