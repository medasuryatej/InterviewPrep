class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        # my code - TLE
        self.lip = 1 # if all elements are same, then 1 would be the longest increasing path
        # visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # visited = set()
        
        def dfs(i,j, d):
            # if (i,j) in visited:
            #    return
            
            # visited.add((i,j))
            
            self.lip = max(self.lip, d)
            
            for x, y in directions:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[i][j] < matrix[new_i][new_j]:
                    dfs(new_i, new_j, 1+d)
                    
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,1)
                
        return self.lip
        
        """
        # to avoid TLE, I need to reuse the lip computed for a cell by storing the previously seen lip at a cel value

        rows = len(matrix)
        cols = len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        
        # default lip path of 0 for every cell in matrix
        lip = [[0 for c in range(cols)] for r in range(rows)]
        
        def dfs(i,j):
            # is a cell already visited, that is lip present for a cel
            if lip[i][j] != 0:
                return lip[i][j]
            
            # lets set initial lip value of 1
            lip[i][j] = 1
            
            for x, y in directions:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[i][j] < matrix[new_i][new_j]:
                    # now update the lip of the cell based on dfs
                    lip[i][j] = max(lip[i][j], 1 + dfs(new_i, new_j))
                    
            return lip[i][j]
                    
        for r in range(rows):
            for c in range(cols):
                dfs(r,c)
                
        # for row in lip:
        #     print(row)
                
        lpath = 1
        
        for r in range(rows):
            for c in range(cols):
                lpath = max(lpath, lip[r][c])

        return lpath
            