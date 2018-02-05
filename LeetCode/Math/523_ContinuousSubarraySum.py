class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # (a+(n*x))%x is same as (a%x)
        # For e.g. in case of the array [23,2,6,4,7] the running sum is [23,25,31,35,42] 
        # and the remainders are [5,1,1,5,0]. 
        # We got remainder 5 at index 0 and at index 3. That means, in between these two indexes we must have added a number which is multiple of the k.
        r = 0
        seen = {0: -1}
        for i, num in enumerate(nums):
            r = (r + num) % k if k else r + num
            if r not in seen: seen[r] = i
            if i - seen[r] > 1: return True
        return False