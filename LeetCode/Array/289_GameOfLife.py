class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getNeighbors(board, i, j, m, n):
            count = 0
            if i > 0:
                if j > 0:
                    count += 1 if board[i-1][j-1] & 1 else 0
                count += 1 if board[i-1][j] & 1 else 0
                if j < n-1:
                    count += 1 if board[i-1][j+1] & 1 else 0
            if i < m-1:
                if j > 0:
                    count += 1 if board[i+1][j-1] & 1 else 0
                count += 1 if board[i+1][j] & 1 else 0
                if j < n-1:
                    count += 1 if board[i+1][j+1] & 1 else 0
            if j > 0:
                count += 1 if board[i][j-1] & 1 else 0
            if j < n-1:
                count += 1 if board[i][j+1] & 1 else 0
            return count
        
        ############################################
        # 0, 1 = unchanged, 2 = 0 to 1, 3 = 1 to 0 #
        ############################################
        if not any(board):
            return
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                count = getNeighbors(board, i, j, m, n)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 3
                else:
                    if count == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
        