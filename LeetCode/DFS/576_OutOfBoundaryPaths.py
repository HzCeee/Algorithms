class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        memo = {}
        
        # return the number of paths to move the ball out of grid boundary.
        def findPathsHelper(curRow, curCol, stepsToMove):
            if (curRow, curCol, stepsToMove) in memo:
                return memo[(curRow, curCol, stepsToMove)]
            
            if not (0 <= curRow <= m - 1 and 0 <= curCol <= n - 1):
                memo[(curRow, curCol, stepsToMove)] = 1
                return memo[(curRow, curCol, stepsToMove)]
            
            if stepsToMove == 0:
                memo[(curRow, curCol, stepsToMove)] = 0
                return memo[(curRow, curCol, stepsToMove)]
            
            count = 0
            for (row, col) in [(curRow - 1, curCol), (curRow + 1, curCol), (curRow, curCol + 1), (curRow, curCol - 1)]:
                count += findPathsHelper(row, col, stepsToMove-1)
            memo[(curRow, curCol, stepsToMove)] = count
            
            return memo[(curRow, curCol, stepsToMove)]
        
        return findPathsHelper(i, j, N) % (10 ** 9 + 7) 
        