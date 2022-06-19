class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curSum = 0
        pointer = 0
        for bit in s[::-1]:
            if bit == "0":
                pointer += 1
            else:
                curValue = 2**pointer
                if curSum + curValue <= k:
                    curSum += curValue
                    pointer += 1
        return pointer