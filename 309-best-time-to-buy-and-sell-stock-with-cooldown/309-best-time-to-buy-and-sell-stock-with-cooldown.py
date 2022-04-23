class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at any given day we have two options one cooldown or one to buy/sell
        hashMap = {} # [index, operation] = profit
        def backTrack(index, canBuy):
            if index >= len(prices):
                return 0
            
            if (index, canBuy) in hashMap:
                return hashMap[(index, canBuy)]
            
            # if you want to cool down
            cooldown = backTrack(index+1, canBuy) # continue the operation
            
            if canBuy:
                # made purchase of stock : subtract the current stock price
                buy = backTrack(index+1, False) - prices[index]
                profit = max(buy, cooldown)
            else:
                # selling it: cooling down cant buy the immediate day
                sell = backTrack(index+2, True) + prices[index]
                profit = max(sell, cooldown)
                
            hashMap[(index, canBuy)] = profit
            return profit
        return backTrack(0, True)