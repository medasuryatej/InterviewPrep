class Solution:
    def __init__(self):
        self.result = 0
        
    def totalNQueens(self, n: int) -> int:
        colSet = set()
        posDiag = set()
        negDiag = set()
        # board = [["." for c in range(n)] for r in range(n)]
        
        def backtrack(r):
            if r == n:
                self.result += 1
                return
            for i in range(n):
                if i in colSet or (r+i) in posDiag or (r-i) in negDiag:
                    continue
                colSet.add(i)
                posDiag.add(r+i)
                negDiag.add(r-i)
                backtrack(r+1)
                colSet.remove(i)
                posDiag.remove(r+i)
                negDiag.remove(r-i)
        backtrack(0)
        return self.result