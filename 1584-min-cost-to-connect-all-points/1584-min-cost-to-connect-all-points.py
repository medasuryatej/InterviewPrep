class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    def getNumPoints(self, points):
        return len(points)
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numPoints = self.getNumPoints(points)
        
        adj_list = { pointIdx: list() for pointIdx in range(numPoints)}
        
        # construct adj list
        for i in range(numPoints):
            pA = Point(points[i][0], points[i][1])
            for j in range(i+1, numPoints):
                pB = Point(points[j][0], points[j][1])
                distance = self.getManhattanDistance(pA, pB)
                # add distances to the list
                adj_list[i].append([distance, j])
                # since these are undirected edges store the same for other point
                adj_list[j].append([distance, i])
                
        minCost = 0
        minHeap = [[0, 0]] # cost, indexofNode
        visitedSet = set()
        
        while len(visitedSet) < numPoints:
            cost, node = heapq.heappop(minHeap)
            if node in visitedSet:
                continue
            minCost += cost
            visitedSet.add(node)
            for dist, neighbor in adj_list[node]:
                heapq.heappush(minHeap, [dist, neighbor])
                
        return minCost
    
    def getManhattanDistance(self, pA, pB):
        return abs(pA.x - pB.x) + abs(pA.y - pB.y)