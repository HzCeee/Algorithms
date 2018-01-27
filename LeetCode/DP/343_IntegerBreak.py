class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[num] denotes the maximum product when n equals to num
        # max([max(num - i, dp[num - i]) * max(i, dp[i]) for i in range(1, num // 2 + 1)])
        
        dp = [1 for i in range(n + 1)]
        
        for num in range(3, n + 1):
            dp[num] = max([max(num - i, dp[num - i]) * max(i, dp[i]) for i in range(1, num // 2 + 1)])
        
        return dp[n]