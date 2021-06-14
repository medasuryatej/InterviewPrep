class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):
            # if a pattern already in cache return its value
            if (i,j) in cache:
                return cache[(i,j)]
            
            # if reached out of bounds in string and pattern
            if i >= len(s) and j >= len(p):
                return True
            
            # reached out of bounds for pattern but not string
            if j >= len(p):
                return False
            
            # check for match
            # if we are in bounds of string and a char match between string
            # and pattern or if a pattern char is "."
            match = (i < len(s)) and ((s[i] == p[j]) or p[j] == ".") 
            
            # checking what is the next character
            if (j+1) < len(p) and p[j+1] == "*":
                # either choose the acceptance of * or don't accept it
                # if not accepted increment j by 2, else increment i by 1
                cache[(i,j)] =  dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i,j)]
            
            # if next char is not *
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)] 
                
            cache[(i,j)] = False
            return False
        return dfs(0,0)
            
            
            
        