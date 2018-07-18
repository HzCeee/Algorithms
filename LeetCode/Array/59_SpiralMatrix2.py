class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[1 for _ in range(n)] for _ in range(n)]
        
        minRow, maxRow, minCol, maxCol = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        count, maxCount = 1, (maxRow + 1) * (maxCol + 1)
        step, stepChoice = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0
        curRow, curCol = 0, 0
        
        while count < maxCount:
            count += 1
            tryRow, tryCol = curRow + step[stepChoice][0], curCol + step[stepChoice][1]
            if not (minRow <= tryRow <= maxRow and minCol <= tryCol <= maxCol):
                stepChoice = stepChoice + 1 if stepChoice + 1 <= 3 else 0 
                if tryRow > maxRow: maxCol -= 1
                elif tryRow < minRow: minCol += 1
                elif tryCol > maxCol: minRow += 1
                elif tryCol < minCol: maxRow -= 1
            curRow, curCol = curRow + step[stepChoice][0], curCol + step[stepChoice][1]
            matrix[curRow][curCol] = count
        
        return matrix

