class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxInt = 2**31 - 1
        return min(int(dividend / divisor), maxInt)