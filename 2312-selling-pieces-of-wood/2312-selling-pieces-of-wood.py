class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # dp = [[0] * (n+1)] * (m+1)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for h,w,p in prices:
            dp[h][w] = p
            
        for r in range(1, m+1):
            for c in range(1, n+1):
                # money = dp[h][w]
                # horizontal cuts
                for nc in range(1, c//2 + 1):
                    dp[r][c] = max(dp[r][c], dp[r][nc] + dp[r][c-nc])
                    
                for nr in range(1, r//2 + 1):
                    dp[r][c] = max(dp[r][c], dp[nr][c] + dp[r-nr][c])
                # vertical cuts
                
                # update new dp value
                # dp[h][w] = money
        return dp[m][n]