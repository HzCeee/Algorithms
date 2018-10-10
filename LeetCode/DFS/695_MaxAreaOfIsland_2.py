class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        maxRow, maxCol = len(grid)-1, len(grid[0])-1
        
        def maxAreaOfIslandHelper(row, col):
            grid[row][col] = 0
            area = 1
            for i, j in [(row, col+1), (row, col-1), (row-1, col), (row+1, col)]:
                if 0 <= i <= maxRow and 0 <= j <= maxCol and grid[i][j] == 1:
                    area += maxAreaOfIslandHelper(i, j)
            return area
        
        maxArea = 0
        for row in range(maxRow+1):
            for col in range(maxCol+1):
                if grid[row][col] == 1:
                    area = maxAreaOfIslandHelper(row, col)
                    if area > maxArea:
                        maxArea = area
                    
        return maxArea