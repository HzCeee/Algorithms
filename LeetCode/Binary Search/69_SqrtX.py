class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        
        while low <= high:
            mid = (low + high) // 2
            squareMid = mid ** 2
            if squareMid == x:
                return mid
            elif squareMid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high