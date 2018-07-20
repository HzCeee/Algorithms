class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # return list of combinations of #count numbers
        def subsetsHelper(leftmostIndex, count):
            if count == 0:
                return [[]]
            
            res = []
            for index in range(leftmostIndex, len(nums) - count + 1):
                for combination in subsetsHelper(index + 1, count - 1):
                    res.append([nums[index]] + combination)
            
            return res
        
        res = [[]]
        for count in range(1, len(nums) + 1):
            res += subsetsHelper(0, count)
        
        return res
                