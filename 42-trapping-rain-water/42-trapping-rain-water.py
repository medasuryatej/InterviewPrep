class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        leftRes = []
        for i in range(len(height)):
            leftRes.append(maxLeft)
            maxLeft = max(height[i], maxLeft)
        # print(leftRes)
        for i in range(len(height)-1, -1, -1):
            leftRes[i] = min(leftRes[i], maxRight)
            maxRight = max(maxRight, height[i])
        # print(leftRes)
        for i in range(len(height)):
            if height[i] < leftRes[i]:
                leftRes[i] = leftRes[i] - height[i]
            else:
                leftRes[i] = 0
        # print(leftRes)
        return sum(leftRes)