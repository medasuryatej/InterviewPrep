class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        counter = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                maxOnes = max(counter, maxOnes)
                counter = 0
        maxOnes = max(counter, maxOnes)
        return maxOnes