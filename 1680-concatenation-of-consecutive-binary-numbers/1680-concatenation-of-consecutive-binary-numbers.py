class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # brute force
        binrep = [bin(i)[2:] for i in range(1, n+1)]
        return int("".join(binrep), 2) % ((10 ** 9) + 7)