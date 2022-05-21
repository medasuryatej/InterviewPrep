class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        if len(nums) < 2: return len(nums)
        slow, fast = 2, 2

        while fast < len(nums):
            print(f"slow-{slow}, fast-{fast}")
            print(nums)
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        """
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i