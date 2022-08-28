class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # y-y1 = (y2-y1)/(x2-x1) * (x-x1)
        p1,p2,p3 = points
        return (p3[1]-p1[1]) * (p2[0]-p1[0]) != ((p2[1]-p1[1])) * (p3[0]-p1[0])  