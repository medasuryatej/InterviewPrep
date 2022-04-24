class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # referred NeetCode solution
        # initially all prices are inf
        prices = [float("inf")] * n
        # price to start from source is 0
        prices[src] = 0
        
        for stop in range(k+1):
            currStopPrices = prices.copy()
            for sr, ds, pr in flights:
                # if a price to reach a place is inf nothing can be done
                if prices[sr] == float("inf"):
                    continue
                # if a price to reach a place + journey price is lower that price to reach dst
                # update the dest price
                if prices[sr] + pr < currStopPrices[ds]:
                    currStopPrices[ds] = prices[sr] + pr
            # update prices after current stop
            prices = currStopPrices
            
        # return dest price
        return prices[dst] if prices[dst] != float("inf") else -1