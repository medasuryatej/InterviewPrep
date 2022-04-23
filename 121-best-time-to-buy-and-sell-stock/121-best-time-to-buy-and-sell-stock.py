class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            # nothing can be sold on sameday
            return 0
        left, right = prices[0], prices[1]
        if len(prices) == 2:
            if right < left:
                return 0
        maxProfit = 0
        for j in range(1, len(prices)):
            right = prices[j]
            maxProfit = max(maxProfit, right - left)
            left = min(left, right)
        return maxProfit