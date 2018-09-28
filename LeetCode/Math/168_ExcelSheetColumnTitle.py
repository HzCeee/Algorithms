class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n /= 26
        return r