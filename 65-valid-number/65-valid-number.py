class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            a = float(s)
            if (a == float("inf") or a == float("-inf")) and "inf" in s.lower() :
                return False
            return True
        except:
            return False