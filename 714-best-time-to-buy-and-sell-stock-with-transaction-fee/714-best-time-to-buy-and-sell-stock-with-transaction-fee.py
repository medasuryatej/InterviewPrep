"""
case 1: I have stock on day i - max of below two cases
    case 1-1: I brought stock today
                    # balance   # stock_price   # trans fee 
        dp[i][1] = dp[i-1][0] - prices[i] - fee
    case 1-2: I am holding stock from yesterday
        dp[i][1] = dp[i-1][1] 
case 2: I don't have stock on day i
    case 2-1: I sold my stock today - max of below two cases
                    # balance  # stock_price
        dp[i][0] = dp[i-1][1] + prices[i]
    case 2-2: I am holding the same state from yesterday
        dp[i][0] = dp[i-1][0]


"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        BUY = 1
        SOLD = 0
        DAY_0 = 0
        DAY_1 = 1
        STATES = [SOLD, BUY]
        # dp = [[0 for p in range(len(prices))] for j in range(len(STATES))]
        dp = [[0 for state in range(len(STATES))] for p in range(len(prices))]
        # init
        dp[DAY_0][SOLD] = 0                       # 0,0
        dp[DAY_0][BUY] = -prices[DAY_0] - fee     # 0,1
        
        for day in range(1, len(prices)):
            # print(dp)
            # print(day)
            dp[day][0] = max(dp[day-1][1] + prices[day], dp[day-1][0])
            dp[day][1] = max(dp[day-1][0] - prices[day] - fee, dp[day-1][1])
            
        # we don't want to hold any stock on last day
        return dp[-1][0]