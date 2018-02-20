class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        blockQueue, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                else:
                    blockQueue.append((i, j))
        
        while blockQueue:
        # for row, col in blockQueue:
            row, col = blockQueue.pop(0)
            for curRow, curCol in ((row, 1+col), (row, col-1), (row+1, col), (row-1, col)):
                distance = matrix[row][col] + 1
                if 0 <= curRow < m and 0 <= curCol < n and distance < matrix[curRow][curCol]:
                    matrix[curRow][curCol] = distance
                    blockQueue.append((curRow, curCol))
                    
        return matrix