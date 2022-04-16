class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(board, r, c):
            if board[r][c] != "O":
                return
            board[r][c] = "A"
            if r > 0: dfs(board, r-1, c)
            if c > 0: dfs(board, r, c-1)
            if r < rows-1: dfs(board, r+1, c)
            if c < cols-1: dfs(board, r, c+1)
        # 0th row
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(board, 0, c)
        # 0th col
        for r in range(1, rows):
            if board[r][0] == 'O':
                dfs(board, r, 0)
        # last col
        for c in range(1, cols):
            if board[rows-1][c] == 'O':
                dfs(board, rows-1, c)
        # last row
        for r in range(1, rows-1):
            if board[r][cols-1] == 'O':
                dfs(board, r, cols-1)
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "A":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
                else:
                    pass
        