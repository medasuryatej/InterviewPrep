class Solution:
    def longestPalindrome(self, s: str) -> int:
        maxLen = 0
        from collections import Counter
        for value in Counter(s).values():
            # adding even interations of a value
            maxLen += value // 2 * 2 # partnered
            if maxLen % 2 == 0 and value % 2 == 1:
                maxLen += 1 # unique center
        return maxLen