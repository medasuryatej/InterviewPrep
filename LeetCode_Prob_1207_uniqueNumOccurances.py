class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        item = Counter(arr).values()
        return len(item) == len(set(item))