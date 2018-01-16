class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # dp[row][col] denotes maximum square side length with matrix[row][col] as right bottom point
        # if matrix[row][col] == 1: dp[row][col] = min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]) + 1
        # else: dp[row][col] = 0
        
        if not matrix:
            return 0
        
        dp = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)]
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]) + 1
                else:
                    dp[row][col] = 0
                    
        return max([max(row) for row in dp]) ** 2