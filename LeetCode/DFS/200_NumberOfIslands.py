class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        maxRow, maxCol = len(grid)-1, len(grid[0])-1
        def numIslandsHelper(row, col):
            grid[row][col] = "0"
            for i, j in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]:
                if 0 <= i <= maxRow and 0 <= j <= maxCol and grid[i][j] == "1":
                    numIslandsHelper(i, j)
        
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islandCount += 1
                    numIslandsHelper(row, col)
        
        return islandCount