class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # referred Neetcode
        # this is a DP problem.
        # at any index (i,j) in (s,t) if both chars equal 
        #    there are two branches, to consider i and move to i+1 and j+1. 
        #    to skip i and move to i+1, j
        
        # memoization
        dp = defaultdict(int)
        
        @cache
        def backtrack(i, j):
            
            # if reached end of t
            if j == len(t): return 1
            
            # if reached end of s and there is still t left its incorrect path
            if i == len(s): return 0
            
            # cehck if already in cache
            if (i, j) in dp: return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = backtrack(i+1, j+1) + backtrack(i+1, j)
            else:
                dp[(i,j)] = backtrack(i+1, j)
                
            return dp[(i, j)]
        
        return backtrack(0, 0)