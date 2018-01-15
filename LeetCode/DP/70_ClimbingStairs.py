class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp[i] denotes the number of ways to climb to the floor i.
        # dp[i] = dp[i - 1] + dp[i - 2]
        
        dp = [1 for i in range(n + 1)]
        
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]