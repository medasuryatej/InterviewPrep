class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        left, right = 0,0
        maxEraseValue = 0
        curSum = 0
        while right  < len(nums):
            if nums[right] not in visited:
                visited.add(nums[right])
                curSum += nums[right]
                right += 1
            else:
                while nums[right] in visited:
                    visited.remove(nums[left])
                    curSum -= nums[left]
                    left += 1
            maxEraseValue = max(maxEraseValue, curSum)
        return maxEraseValue