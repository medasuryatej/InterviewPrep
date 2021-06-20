class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sorting children and cookie sizes
        g = sorted(g)
        s = sorted(s)
        c,k = 0,0
        satisfied = 0
        while c < len(g) and k < len(s):
            if g[c] <= s[k]:
                c += 1
                k += 1
                satisfied += 1
            else:
                k += 1
        return satisfied
        