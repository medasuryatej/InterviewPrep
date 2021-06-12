class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start + 2*0
        for j in range(1, n):
            result ^= (start + (2*j))
        return result