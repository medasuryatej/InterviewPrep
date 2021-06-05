class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for j in range(1, len(nums)+1):
            val ^= j
        given = nums[0]
        for i in range(1, len(nums)):
            given ^= nums[i]
        return val ^ given