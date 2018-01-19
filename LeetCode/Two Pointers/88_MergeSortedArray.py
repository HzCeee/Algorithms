class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # index1 denotes the index of current compared numbers in nums1
        # index2 denotes the index of current compared numbers in nums2
        # curIndex denotes the index of current processed numbers in new nums1
        
        index1, index2, curIndex = m - 1, n - 1, m + n - 1
        
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[curIndex] = nums1[index1]
                index1 -= 1
                curIndex -= 1
            else:
                nums1[curIndex] = nums2[index2]
                index2 -= 1
                curIndex -= 1
        if index2 >= 0:
            nums1[:index2 + 1] = nums2[:index2 + 1]