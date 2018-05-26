class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        
        toPacific, toAtlantic = set(), set()
        maxRow, maxCol = len(matrix) - 1, len(matrix[0]) - 1
        
        def pacificAtlanticHelper(row, col, flowToPacific):
            if (row, col) in visited:
                return
            visited.add((row, col))
            
            flowTo = toPacific if flowToPacific else toAtlantic
            flowTo.add((row, col))
            for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= i <= maxRow and 0 <= j <= maxCol and matrix[i][j] >= matrix[row][col]:
                    pacificAtlanticHelper(i, j, flowToPacific)
        
        for col in range(maxCol + 1):
            visited = set(); pacificAtlanticHelper(0, col, True)
            visited = set(); pacificAtlanticHelper(maxRow, col, False)
        for row in range(maxRow + 1): 
            visited = set(); pacificAtlanticHelper(row, 0, True)
            visited = set(); pacificAtlanticHelper(row, maxCol, False)
        ans = []
        for row, col in toPacific.intersection(toAtlantic):
            ans.append([row, col])
            
        return ans