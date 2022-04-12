class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        next_state = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                neighbors = self.getNeighbors(board, i, j, m, n)
                # print(i,j, neighbors)
                if board[i][j] == 1:
                    # if current cell is alive
                    if neighbors < 2:
                        # under population
                        next_state[i][j] = 0
                    elif neighbors <= 3:
                        next_state[i][j] = board[i][j]
                    else:
                        # over population
                        next_state[i][j] = 0
                else:
                    if neighbors == 3:
                        # reproduction
                        # print(i,j, neighbors)
                        next_state[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = next_state[i][j]
        
        
        
    def getNeighbors(self, board, i, j, m, n):
        # eight neighbors
        # left, right (i,j-1), (i,j+1)
        # up , down, (i-1,j), (i+1,j)
        # diagonal left-up, left-down, (i-1,j-1), (i+1,j-1)
        # diagonal right-up, right-down (i-1, j+1), (i+1, j+1)
        neighbors = []
        # left
        if 0 <= j-1 < n:
            neighbors.append(board[i][j-1])
            # upper-left
            if 0 <= i-1 < m:
                neighbors.append(board[i-1][j-1])
            # lower-left
            if 0 <= i+1 < m:
                neighbors.append(board[i+1][j-1])
        # right
        if 0 <= j+1 < n:
            neighbors.append(board[i][j+1])
            # upper-right
            if 0 <= i-1 < m:
                neighbors.append(board[i-1][j+1])
            # lower-right
            if 0 <= i+1 < m:
                neighbors.append(board[i+1][j+1])
        # up
        if 0 <= i-1 < m:
            neighbors.append(board[i-1][j])
        # down
        if 0 <= i+1 < m:
            neighbors.append(board[i+1][j])
            
        return sum(neighbors)
        
        
        
        