class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        if matrix is None or not matrix:
            return
        
        # dp[row][col] denotes the area of rectangle with matrix[row][col] as lower right corner 
        # and matrix[0][0] as upper left corner
        # dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + matrix[row][col]
        
        self.dp = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)]
        for row in range(len(self.dp)):
            for col in range(len(self.dp[0])):
                self.dp[row][col] = self.dp[row - 1][col] + self.dp[row][col - 1] - self.dp[row - 1][col - 1] + matrix[row - 1][col - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)