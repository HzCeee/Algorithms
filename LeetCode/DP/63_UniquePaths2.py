class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
    
        # dp[row][col] denote the number of unique paths from top-left corner to the point in grid[row][col]
        # if obstacleGrid[row][col] == 1: dp[row][col] = 0
        # else: dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0 for col in range(n)] for row in range(m)]
        
        for col in range(n):
            if obstacleGrid[0][col] == 1:
                break
            dp[0][col] = 1
            
        for row in range(m):
            if obstacleGrid[row][0] == 1:
                break
            dp[row][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1: 
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                
        return dp[-1][-1]