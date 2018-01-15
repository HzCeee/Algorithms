class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # dp[row][col] denotes the minimum path sum from top to triangle[row][col]
        # dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
        
        maxValue = float('inf')
        
        dp = [[maxValue] + row + [maxValue] for row in triangle]
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row]) - 1):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col - 1]
                
        return min(dp[-1][1:-1])
        