class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextGreaterNum = {}
        for i, curNum in enumerate(nums2):
            for num in nums2[:i]:
                if num not in nextGreaterNum and curNum > num:
                    nextGreaterNum[num] = curNum
        
        return [nextGreaterNum.get(num, -1) for num in nums1]