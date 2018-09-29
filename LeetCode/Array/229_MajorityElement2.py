class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsCount = dict()
        output = set()
        for num in nums:
            if num not in numsCount:
                numsCount[num] = 0
            numsCount[num] += 1
            if numsCount[num] > len(nums) // 3:
                output.add(num)
        
        return list(output)