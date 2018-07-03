class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        while A[i] < A[i + 1]:
            i += 1
        return i