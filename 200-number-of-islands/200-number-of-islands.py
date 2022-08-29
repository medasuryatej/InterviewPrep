class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islandCount = 0
        def dfs(r, c):
            # point is zero or visited or boundaries
            if r < 0 or c < 0 or r == len(grid) or c ==len(grid[0]) or grid[r][c] == "0" or grid[r][c] == -1:
                return
            grid[r][c] = -1 # visited
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        # iterate over all points
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[0])):
                # check for ones alone
                if grid[rowIndex][colIndex] == "1": 
                    dfs(rowIndex, colIndex)
                    self.islandCount += 1
        print(grid)
        return self.islandCount
        