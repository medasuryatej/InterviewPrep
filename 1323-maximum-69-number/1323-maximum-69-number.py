class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = list(str(num))
        if "6" in nums:
            nums[nums.index("6")] = "9"
            return int("".join(nums))
        return num