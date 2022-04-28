class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = max(weights)
        maxCap = sum(weights)
        
        def canShip(capacity):
            days_needed = 0
            curWeights = 0
            for w in weights:
                curWeights += w
                
                if curWeights > capacity:
                    days_needed += 1
                    curWeights = w
                    if days_needed > days-1:
                        return False
            return days_needed < days
        
        while minCap < maxCap:
            avgCap = (minCap + maxCap) // 2
            
            if canShip(avgCap):
                maxCap = avgCap
            else:
                minCap = avgCap + 1
                
        return maxCap