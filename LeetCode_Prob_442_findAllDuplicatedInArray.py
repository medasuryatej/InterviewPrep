class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            if nums[abs(nums[i])-1] < 0:
                # already visited => duplicate
                output.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
        return output
            