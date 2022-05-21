class Solution:
    def sumZero(self, n: int) -> List[int]:
        maxPos = n // 2
        if n % 2 == 0:
            return list(range(-maxPos, 0, 1)) + list(range(1, maxPos+1))
        else:
            return list(range(-maxPos, 0, 1)) + list(range(0, maxPos+1))