class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # dp[row][col] denote the number of unique paths from top-left corner to the point in grid[row][col]
        # dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        dp = [[1 for col in range(n)] for row in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                
        return dp[-1][-1]