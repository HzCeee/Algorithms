class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        maxRow, maxCol = len(board) - 1, len(board[0]) - 1
        
        def adjacentMines(row, col):
            count = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i <= maxRow and 0 <= j <= maxCol and board[i][j] == "M":
                        count += 1
            return count
        
        def updateBoardHelper(row, col):
            if not(0 <= row <= maxRow) or not(0 <= col <= maxCol): return
            
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                count = adjacentMines(row, col)
                if count > 0: 
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    for i in range(row - 1, row + 2):
                        for j in range(col - 1, col + 2):
                            updateBoardHelper(i, j)
        
        updateBoardHelper(*click)
        
        return board