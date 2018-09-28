class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count=0
        while(n != m):
            n >>= 1
            m >>= 1
            count += 1
        return m << count