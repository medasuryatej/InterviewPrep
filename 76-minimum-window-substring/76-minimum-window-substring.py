from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # referred solution
        # if either of the strings is empty
        if s == "" or t == "":
            # return empty string
            return ""
        
        tCharFreq = Counter(t)
        
        # num unique chars needed in substring
        numUniqReq = len(tCharFreq)
        formed = 0
        
        left, right = 0, 0
        
        # minWindowLength, left and right pointer positions
        finalResult = float("inf"), None, None
        
        # to keep track of char freq in the current window
        curWindowCount = defaultdict(int)
        
        # iterate until right pointer reaches end
        while right < len(s):
            # get the character
            character = s[right]
            # increment its count
            curWindowCount[character] += 1
            
            if character in tCharFreq and curWindowCount[character] == tCharFreq[character]:
                # found one unique character
                formed += 1
                
            # shrinking from left
            while left <= right and formed == numUniqReq:
                character = s[left]
                # update answer
                if right - left + 1 < finalResult[0]:
                    finalResult = (right - left + 1, left, right)
                
                curWindowCount[character] -= 1
                if character in tCharFreq and curWindowCount[character] < tCharFreq[character]:
                    formed -= 1
                    
                left += 1
            right += 1
            
        return "" if finalResult[0] == float("inf") else s[finalResult[1]: finalResult[2] + 1]
            