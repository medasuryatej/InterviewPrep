class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # first sort based on width and then sort in reverse based on height
        sortedEnvelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        # now perform LIS on the heights
        heights = [height for width, height in sortedEnvelopes]
        
        return self.lengthOfLIS(heights)
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
        # print(lis)
        return len(lis)