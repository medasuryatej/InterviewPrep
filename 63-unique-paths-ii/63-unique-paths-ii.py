class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        OBSTACLE = 1
        BLOCKED = 0
        
        # if origin has obstacle
        #   # then zero moves
        if obstacleGrid[0][0] == OBSTACLE:
            return 0
        
        dp = [[0 for c in range(cols)] for r in range(rows)]
        
        dp[0][0] = 1
        
        # 0th row
        for c in range(1, cols):
            # if previous cell is blocked or current cell has obstacle
            #   # then no path possble
            if obstacleGrid[0][c] == OBSTACLE or dp[0][c-1] == BLOCKED:
                continue
            dp[0][c] = 1
            
        # 0th col
        for r in range(1, rows):
            if obstacleGrid[r][0] == OBSTACLE or dp[r-1][0] == BLOCKED:
                continue
            dp[r][0] = 1
            
        # iterate over every other row and col
        for r in range(1, rows):
            for c in range(1, cols):
                # if current cell has obstacle
                if obstacleGrid[r][c] == OBSTACLE:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                    
        return dp[-1][-1]