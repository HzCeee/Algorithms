class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        mid = (left + right) // 2
        leftMaxSum = self.maxSubArray(nums[: mid+1])
        rightMaxSum = self.maxSubArray(nums[mid+1:])
        
        leftInterSum, leftMaxInterSum = 0, -float('inf')
        for index in range(mid + 1)[::-1]:
            leftInterSum += nums[index]
            leftMaxInterSum = max(leftInterSum, leftMaxInterSum)
        
        rightInterSum, rightMaxInterSum = 0, -float('inf')
        for index in range(mid + 1, len(nums)):
            rightInterSum += nums[index]
            rightMaxInterSum = max(rightInterSum, rightMaxInterSum)
        
        midMaxSum = leftMaxInterSum + rightMaxInterSum
        
        return max(leftMaxSum, rightMaxSum, midMaxSum)