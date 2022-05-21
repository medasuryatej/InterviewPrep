class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dynamic programming bottom up approach
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for am in range(1, amount+1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am], 1 + dp[am-coin])
        # if we are not able to achieve min coin reach, then returining -1
        return dp[amount] if dp[amount] != (amount+1) else -1
                
                
        