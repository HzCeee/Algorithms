class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        maxRow, maxCol = len(board) - 1, len(board[0]) - 1
        def getNeighbors(row, col):
            neighbors = []
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    if 0 <= i <= maxRow and 0 <= j <= maxCol and not (i == row and j == col):
                        neighbors.append([i, j])
            return neighbors
        
        def updateBoardHelper(board, click, visitedBlock):
            if tuple(click) in visitedBlock:
                return
            visitedBlock.add(tuple(click))
            
            row, col = click
            
            mineCount = 0
            neighbors = getNeighbors(row, col)
            
            for i, j in neighbors:
                if board[i][j] == "M" or board[i][j] == "X":
                    mineCount += 1
                    
            if mineCount == 0:
                board[row][col] = "B"
                for neighbor in neighbors:
                    updateBoardHelper(board, neighbor, visitedBlock)
            else:
                board[row][col] = str(mineCount)
        
        updateBoardHelper(board, click, set())
        
        return board
                
            