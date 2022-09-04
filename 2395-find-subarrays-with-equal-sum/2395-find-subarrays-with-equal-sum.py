class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumSet = set()
        for i in range(1, len(nums)):
            subSum = nums[i] + nums[i-1]
            if subSum in sumSet:
                return True
            sumSet.add(subSum)
        return False