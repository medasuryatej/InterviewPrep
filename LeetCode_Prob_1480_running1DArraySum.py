class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res_sum = 0
        for i in range(len(nums)):
            res_sum += nums[i]
            nums[i] = res_sum
        return nums