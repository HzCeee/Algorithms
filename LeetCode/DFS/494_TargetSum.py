class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        self.memo = {}
        
        # return the number of ways to make sum of integers equal to target.
        def findTargetSumWaysHelper(nums, target):
            if str((nums, target)) in self.memo:
                return self.memo[str((nums, target))]
            
            if len(nums) == 1:
                if nums[0] == target and nums[0] == -target:
                    return 2
                elif nums[0] == target or nums[0] == -target:
                    return 1
                else:
                    return 0
            
            self.memo[str((nums, target))] = \
            findTargetSumWaysHelper(nums[1:], target - nums[0]) + findTargetSumWaysHelper(nums[1:], target + nums[0])
            
            return self.memo[str((nums, target))]
        
        return findTargetSumWaysHelper(nums, S)