class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # dp[i] denotes the total number of ways to paint i posts with k colors
        # dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        if n <= 2:
            return 0 if k == 0 or n == 0 else k**n
        if n > 2 and k <= 1:
            return 0
        
        prevNumWays, curNumWays = k, k*k
        for i in range(3, n+1):
            curNum = prevNumWays * (k-1) + curNumWays * (k-1)
            prevNumWays, curNumWays = curNumWays, curNum
        
        return curNumWays