class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return sorted(c, key=lambda x: c[x], reverse=True)[:k]