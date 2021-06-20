class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3: return max(nums)
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num != first:
                third = second
                second = num
            elif num > third  and num != first and num != second:
                third = num
        return third
                        