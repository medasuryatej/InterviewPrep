class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i < len(s)-1 and (s[i] == "1" or (s[i]=="2" and s[i+1] in "0123456")):
                    dp[i] += dp[i+2]
        return dp[0]
        
        


"""
# recursion TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        # referred solution - recursion
        n = len(s)
        if n == 0: return 0
        return self.decodings(0, s)
    
    def decodings(self, index, s):
        if index == len(s):
            # reached end
            return 1
        if s[index] == '0':
            # first char is 0 - no other way
            return 0
        res = self.decodings(index+1, s)
        # if one more char left
        if (index < len(s)-1):
            # if current is in range(10 - 26) inclusive
            if s[index] == '1' or (s[index] == '2' and int(s[index+1]) < 7):
                res += self.decodings(index+2, s)
        return res
        
"""

"""
        import string
        self.mapper = {str(index+1): char for index, char in enumerate(string.ascii_uppercase)}
        ways = []
        
        for i in range(len(s)-1):
            for j in range(i+1, i+3):
                substr = s[i:j]
                if substr in mapper:
                    ways += 1
        ways += 1 if s[-1] in mapper else 0
        return ways
        
        self.backtrack(s, 0, "", ways)
        print(ways)
        return len(ways)
        """
    
"""
    def backtrack(self, s, index, current, output):
        if index == len(s):
            output.append(current)
            return 
        
        for i in range(index, len(s)):
            c1 = self.mapper.get(s[i], '')
            if (i + 1) < len(s):
                c2 = self.mapper.get(s[i+1], '')
                if c1 and c2:
                    self.backtrack(s, i+1, current + c1, output)
                    self.backtrack(s, i+2, current + c1 + c2, output)
                    # self.backtrack(s, i+2, current + self.mapper[s1])
                    grp = s[i] + s[i+1]
                    if grp in self.mapper:
                        self.backtrack(s, i+2, current + self.mapper[grp], output)
                elif c1 and not c2:
                    grp = s[i] + s[i+1]
                    if grp in self.mapper:
                        self.backtrack(s, i+2, current + self.mapper[grp], output)
                else:
                    return
            else:
                if c1:
                    self.backtrack(s, i+1, current + c1, output)
    """
            