class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        r = Counter(nums)
        return sorted(nums, key= lambda x: (r[x], -x))
        

nums = [2,3,1,3,2]
print(frequencySort(nums))