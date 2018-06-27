class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = {}
        stack = [] # number of nums2 which have not found next greater element
        
        for num in nums2:
            while stack and stack[-1] < num:
                ans[stack.pop()] = num
            stack.append(num)
        return [ans.get(num, -1) for num in nums1]
                