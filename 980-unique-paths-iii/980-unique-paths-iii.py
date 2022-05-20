class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(i,j, walk):        
            if (i,j) in visit:
                # already visited
                return
            
            if i < 0 or i >= rows or j < 0 or j >= cols:
                # out of bounds
                return
            
            if grid[i][j] == -1:
                # obstacle
                return
            
            if grid[i][j] == 2:
                if walk == (empty_cells + 1):
                    self.count += 1
                return
            visit.add((i,j))
            
            # four directions
            dfs(i+1, j, 1+walk)
            dfs(i-1, j, 1+walk)
            dfs(i, j+1, 1+walk)
            dfs(i, j-1, 1+walk)
            
            visit.remove((i,j))
            
        empty_cells = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    x, y = r,c
                elif grid[r][c] == 0:
                    empty_cells += 1
                    
        dfs(x, y, 0)
        return self.count
        