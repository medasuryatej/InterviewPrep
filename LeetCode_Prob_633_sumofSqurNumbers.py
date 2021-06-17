class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        for j in range(0, int(math.sqrt(c)) + 1):
            b = math.sqrt(c - j**2)
            if b == int(b):
                return True
        return False
                