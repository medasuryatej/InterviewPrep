class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        count = Counter(nums)
        result = []
        temp = []
        def dfs():
            if len(temp) == len(nums):
                result.append(temp.copy())
                return 
            for n in count:
                if count[n] > 0:
                    temp.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    temp.pop()
        dfs()
        return result