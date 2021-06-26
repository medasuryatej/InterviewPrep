class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        for j in range(0, len(nums), 2):
            result += nums[j]
        return result