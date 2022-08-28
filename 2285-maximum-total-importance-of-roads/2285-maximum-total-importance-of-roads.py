class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        in_degree = [0]*n
        for road_s, road_e in roads:
            in_degree[road_s] += 1
            in_degree[road_e] += 1
        in_degree.sort()
        result = 0
        for i in range(1, n+1):
            result += in_degree[i-1] * i
        return result