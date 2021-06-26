class Solution:
    def trimMean(self, arr: List[int]) -> float:
        count = len(arr)
        arr = sorted(arr)
        percentRemove = int(0.05*count)
        return sum(arr[percentRemove: count - percentRemove]) / (int(0.9*count))