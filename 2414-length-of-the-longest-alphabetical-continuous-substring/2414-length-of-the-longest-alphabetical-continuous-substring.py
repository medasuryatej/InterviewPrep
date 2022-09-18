import string
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        prevLetter = {}
        prev = ""
        letters = string.ascii_lowercase
        
        if len(s) == 1 or s in letters:
            # base case
            return len(s)
        
        for eachChar in letters:
            prevLetter[eachChar] = prev
            prev = eachChar
            
        left, right = 0, 1
        maxLen = 0
        prev = s[left]
        
        while right < len(s):
            if prevLetter[s[right]] == prev:
                prev = s[right]
                right += 1
            else:
                maxLen = max(maxLen, right - left)
                left = right
                right += 1
                prev = s[left]
                
        maxLen = max(maxLen, right - left)
        return maxLen