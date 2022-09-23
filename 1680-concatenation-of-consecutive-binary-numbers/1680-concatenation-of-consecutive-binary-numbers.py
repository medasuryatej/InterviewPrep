class Solution:
    def concatenatedBinary(self, n: int) -> int:
        prev = 1
        if n == 1:
            return prev
        # curr = prev
        MOD = 10**9 + 7
        for i in range(2, n+1):
            prev <<= (i).bit_length()
            prev += i
            prev %= MOD
            
        return prev