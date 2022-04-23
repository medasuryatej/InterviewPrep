class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create a dp array
        # on first day the profit is zero
        # when zero transactions can be be made the profit is zero
        dp = [[0 for i in range(len(prices))] for j in range(3)]
        # have a variable that keeps track of maxdiff between profit and current trans
        
        # iterate over every transaction
        for trans in range(1, 3):
            # iterate over every price
            maxDiff = 0 - prices[0]
            for day in range(1, len(prices)):
                
                # if transaction is made the profit would be current day price
                # plus the maxdiff
                dp[trans][day] = max(prices[day] + maxDiff, dp[trans][day-1])
                # Either keep holding the stock we bought before, or just buy in today
                maxDiff = max(maxDiff, dp[trans-1][day-1] - prices[day])
        for row in dp:
            print(row)
        # return the last element
        return dp[-1][-1]