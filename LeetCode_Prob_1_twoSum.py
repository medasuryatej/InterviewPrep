class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the numbers
        hashmap = {}
        for index, num in enumerate(nums):
            rem = target - num
            if rem not in hashmap:
                hashmap[num] = index
            else:
                return [hashmap[rem], index]