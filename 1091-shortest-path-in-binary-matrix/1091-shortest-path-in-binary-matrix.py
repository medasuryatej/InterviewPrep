class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        VISITED = 1
        
        origin = grid[0][0]
        destination = grid[rows-1][cols-1]
        
        if origin == 1 or destination == 1:
            # no path
            return -1
        
        queue = [(0, 0, 1)] # x, y, distance
        grid[0][0] = VISITED
        
        for x, y, d in queue:
            if (x, y) == (rows-1, cols-1):
                return d
            for i,j in ((x+1,y), (x-1,y), (x,y+1), (x,y-1), 
                        (x+1, y+1), (x+1, y-1), (x-1,y+1), (x-1, y-1)):
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] != 1:
                    queue.append((i,j,d+1))
                    grid[i][j] = 1
                    
        return -1
            