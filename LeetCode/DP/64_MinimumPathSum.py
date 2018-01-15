class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # dp[row][col] denotes the minimum sum of all numbers along the path from top left to grid[row][col]
        # dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        
        m = len(grid)
        n = len(grid[0])
        
        dp = grid
        
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
            
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
        
        return dp[-1][-1]