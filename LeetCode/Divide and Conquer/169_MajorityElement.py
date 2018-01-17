class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        
        leftMajorityElement = self.majorityElement(nums[: mid+1])
        rightMajorrityElement = self.majorityElement(nums[mid+1:])
        if leftMajorityElement == rightMajorrityElement: return leftMajorityElement
        
        leftCount = sum([1 for num in nums[: mid+1] if num == leftMajorityElement])
        rightCount = sum([1 for num in nums[mid+1:] if num == rightMajorrityElement])
        
        return leftMajorityElement if leftCount > rightCount else rightMajorrityElement