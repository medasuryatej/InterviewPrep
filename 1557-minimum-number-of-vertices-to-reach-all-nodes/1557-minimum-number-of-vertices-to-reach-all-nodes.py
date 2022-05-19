class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
            
        # print(indegree)
            
        output = [index for index, edge in enumerate(indegree) if edge==0]
        
        return output
        