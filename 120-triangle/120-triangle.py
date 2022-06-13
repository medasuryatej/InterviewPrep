class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # referred solution
        # dp bottom up
        minLen = triangle[-1] # last layer
        numLayers = len(triangle) # num layers
        # start from penultimate layer and go to the top
        for n in range(numLayers-2, -1, -1):
            # print(minLen)
            for i in range(n+1):
                # iterate over every cell in the layer
                # kth layer minLen getting updated from (k+1)th layer info
                minLen[i] = min(minLen[i], minLen[i+1]) + triangle[n][i] # min of both children plus current value
        return minLen[0]