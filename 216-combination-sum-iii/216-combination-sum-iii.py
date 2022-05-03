class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []
        temp = []
        def backtrack(k, current, index):
            if k == 0:
                combs.append(current.copy())
                return
            else:
                for i in range(index, 10):
                    current.append(i)
                    backtrack(k-1, current, i+1)
                    current.pop()
                    
        backtrack(k, [], 1)
        
        result = []
        for comb in combs:
            if sum(comb) == n:
                result.append(comb)
                
        return result