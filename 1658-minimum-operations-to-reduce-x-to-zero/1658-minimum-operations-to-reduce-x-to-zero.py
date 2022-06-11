class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if not target: return len(nums)
        res, psum = -1, 0
        hMap = {0 : -1}
        for i in range(len(nums)):
            psum += nums[i]
            if psum - target in hMap:
                res = max(res, i - hMap[psum - target])
            hMap[psum] = i
        return len(nums)-res if res != -1 else -1
        