class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        rN = dict(Counter(ransomNote))
        mg = dict(Counter(magazine))
        for key,val in rN.items():
            if rN[key] > mg.get(key,0):
                return False
        return True