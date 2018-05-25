class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxRow, maxCol = len(grid) - 1, len(grid[0]) - 1
        
        def maxAreaOfIslandHelper(grid, row, col):
            if not (0 <= row <= maxRow) or not (0 <= col <= maxCol) or grid[row][col] != 1:
                return 0
            else:
                grid[row][col] = "X"
                surroundArea = 0
                for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    surroundArea += maxAreaOfIslandHelper(grid, i, j)
                return 1 + surroundArea
        
        maxArea = 0
        for row in range(maxRow + 1):
            for col in range(maxCol + 1):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, maxAreaOfIslandHelper(grid, row, col))
                    
        return maxArea
        