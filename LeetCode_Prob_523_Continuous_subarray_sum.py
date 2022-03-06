class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
            Keep accumulating sums
            for each sum get reminder when divided by k.
            store the reminder in hashmap obtained at a particular index
            if we get same reminder it indicates we have added a multiple of k
            to the sum
            now get the difference of the indices, if its more than 2 return True.
            corner case: if first value itself is a multiple of k, then we need to 
            have an empty sum at index -1, to balance the question of contiguous subarray
        """
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
