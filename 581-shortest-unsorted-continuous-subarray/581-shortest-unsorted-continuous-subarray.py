class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = len(nums)-1
        end = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start > 0 else 0