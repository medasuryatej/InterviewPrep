class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        can_reach_pacific = [[False for col in range(n)] for row in range(m)]
        can_reach_atlantic = [[False for col in range(n)] for row in range(m)]
        
        GO_LEFT = [0, -1]
        GO_RIGHT = [0, 1]
        GO_UP = [-1, 0]
        GO_DOWN = [1, 0]
        
        directions = [GO_LEFT, GO_RIGHT, GO_UP, GO_DOWN]
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for direction in directions:
                new_x, new_y = i + direction[0], j + direction[1]
                if (0 <= new_x < m) and (0 <= new_y < n) and (visited[new_x][new_y] == False) and \
                    (heights[new_x][new_y] >= heights[i][j]):
                    dfs(new_x, new_y, visited)
        
        # first col (pacific) and last col (atlantic)
        for row in range(m):
            dfs(row, 0, can_reach_pacific)
            dfs(row, n-1, can_reach_atlantic)
            
        # first row (pacific) and last row (atlantic)
        for col in range(n):
            dfs(0, col, can_reach_pacific)
            dfs(m-1, col, can_reach_atlantic)
            
        output = []
        
        for row in range(m):
            for col in range(n):
                if can_reach_pacific[row][col] and can_reach_atlantic[row][col]:
                    output.append((row,col))
                    
        return output