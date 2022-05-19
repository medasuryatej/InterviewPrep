class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visit = set()
        for u, v in edges:
            if u in visit:
                return u
            elif v in visit:
                return v
            visit.add(u)
            visit.add(v)