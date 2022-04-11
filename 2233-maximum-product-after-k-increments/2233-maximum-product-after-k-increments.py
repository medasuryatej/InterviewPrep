import heapq as heap
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap.heapify(nums)
        for i in range(k):
            top = heap.heappop(nums)
            heap.heappush(nums, top+1)
        product = 1
        mod = 10**9 + 7
        for num in nums:
            product *= num
            product %= mod
        return product