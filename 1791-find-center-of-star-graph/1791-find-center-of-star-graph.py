class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        visit = set()
        for u, v in edges:
            if u in visit:
                return u
            elif v in visit:
                return v
            visit.add(u)
            visit.add(v)
        """
        firstNode = edges[0]
        secondNode = edges[1]
        if firstNode[0] in secondNode:
            return firstNode[0]
        else:
            return firstNode[1]