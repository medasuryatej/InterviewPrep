class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {nodeIdx : list() for nodeIdx in range(n)}
        
        # add both directional edges to the adj list
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        def dfs(src, dest, seen):
            if src == dest:
                return True
            
            # bidirectional edges, hence to avoid too much recursion
            if src in seen:
                return False
            
            # add node to visited
            seen.add(src)
            
            for neigh in adjList[src]:
                # if any dfs returns true, return True
                if dfs(neigh, dest, seen):
                    return True
                
            return False
        
        seen = set()
        return dfs(source, destination, seen)