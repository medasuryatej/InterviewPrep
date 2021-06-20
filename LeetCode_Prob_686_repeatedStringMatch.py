class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # base case
        # non matching strings
        if not set(b).issubset(set(a)):
            return -1
        # matching string chars
        for i in range(1,int(len(b)/len(a))+3):
            if b in a*i: 
                return i
        return -1