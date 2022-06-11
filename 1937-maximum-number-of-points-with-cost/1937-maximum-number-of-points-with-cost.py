class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        
        dp = points[0]
        left = [0] * cols
        right = [0] * cols
        
        for r in range(1, rows):
            for c in range(cols):
                if c == 0:
                    left[c] = dp[c]
                else:
                    left[c] = max(left[c-1]-1, dp[c])
                    
            for c in range(cols-1, -1, -1):
                if c == cols - 1:
                    right[c] = dp[c]
                else:
                    right[c] = max(right[c+1]-1, dp[c])
            
            for c in range(cols):
                dp[c] = points[r][c] + max(left[c], right[c])
                
        return max(dp)