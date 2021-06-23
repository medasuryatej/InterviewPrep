class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if self.isPrime(area):
            return [area,1]
        else:
            import math
            maxWidth = 0
            for i in range(2, int(math.sqrt(area))+1):
                if area % i == 0:
                    maxWidth = max(maxWidth, i)
            return sorted([area//maxWidth, maxWidth], reverse=True)
        
    def isPrime(self, num):
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True