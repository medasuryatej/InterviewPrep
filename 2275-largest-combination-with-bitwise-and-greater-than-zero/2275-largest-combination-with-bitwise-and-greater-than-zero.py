class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(1 << i & a > 0 for a in candidates) for i in range(30))