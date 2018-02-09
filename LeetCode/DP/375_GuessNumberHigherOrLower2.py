class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[low][high] refers to the minimum money need to guarantee a win within range [low, high]
        # dp[low][high] = min([guess + max(dp[low][guess], dp[guess][high]) for guess in range(low, high)])
        
        dp = [[0] * n for _ in range(n)]
        
        for low in range(n)[::-1]:
            for high in range(low + 1, n):
                tmp = [guess + 1 + max(dp[low][guess - 1], dp[guess + 1][high]) for guess in range(low, high)]
                dp[low][high] = min(tmp) if tmp else 0
        
        return dp[0][-1]