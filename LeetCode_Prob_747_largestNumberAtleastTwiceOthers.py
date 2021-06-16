class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxNum, maxIndex = max(nums) , nums.index(max(nums))
        # totalSum = sum(nums)
        for index, num in enumerate(nums):
            if maxNum < 2*num and index != maxIndex:
                return -1
        return maxIndex