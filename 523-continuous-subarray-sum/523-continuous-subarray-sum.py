class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap = {0 : -1}
        total = 0
        for idx in range(len(nums)):
            total += nums[idx]
            mod = total % k
            if mod in hashMap:
                difference = idx - hashMap[mod]
                if difference >= 2:
                    return True
            else:
                hashMap[mod] = idx
        return False