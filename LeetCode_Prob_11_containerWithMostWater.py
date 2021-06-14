
# Brute Force O(N Square)
def maxArea_Brute(height):
        maxWater = 0
        for i in range(0, len(height) - 1):
            currentArea = 0
            for j in range(i, len(height)):
                currentArea = max(currentArea, (j-i) * min(height[i], height[j]))
            maxWater = max(maxWatPer, currentArea)
        return maxWater


# two pointer approach
def maxArea(height):
    left, right = 0, len(height) - 1
    area = 0
    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
height = [1,1]
print(maxArea(height))
height = [4,3,2,1,4]
print(maxArea(height))
height = [2,3,4,5,18,17,6]
print(maxArea(height))