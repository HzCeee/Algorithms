class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1] * (2 * len(nums))
        stack = [] # stores indices that have not found next greater number
        for i, num in enumerate(2 * nums):
            while stack and nums[stack[-1] % len(nums)] < num:
                ans[stack.pop()] = num
            stack.append(i)
        
        return ans[:len(nums)]