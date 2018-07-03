class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowRows, highRows = 0, n
        while lowRows <= highRows:
            midRows = (lowRows + highRows) // 2
            coinsNumLeast = (1 + midRows) * midRows / 2
            coinsNumMost = (1 + midRows + 1) * (midRows + 1) / 2
            if coinsNumLeast <= n < coinsNumMost:
                return midRows
            elif n == coinsNumMost:
                return midRows + 1
            elif n < coinsNumLeast:
                highRows = midRows - 1
            else:
                lowRows = midRows + 1
                
        return -1