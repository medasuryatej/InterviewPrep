class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums).values()
        for val in c:
            if val % 2 != 0:
                return False
        return True
        