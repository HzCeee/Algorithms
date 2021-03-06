class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # dp[i] denotes the sum of the subarray nums[: index + 1]
        
        self.nums = nums
        self.dp = [0 for i in range(len(nums) + 1)]
        for i in range(1, len(self.dp)):
            self.dp[i] = self.dp[i - 1] + nums[i - 1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)