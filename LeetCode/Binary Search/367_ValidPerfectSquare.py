class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lowPtr, highPtr = 1, num
        while lowPtr <= highPtr:
            mid = (lowPtr + highPtr) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                lowPtr = mid + 1
            else:
                highPtr = mid - 1
        
        return False