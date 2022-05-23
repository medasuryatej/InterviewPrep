class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        visit = set()
        blocked_set = set()
        for block in blocked:
            blocked_set.add(tuple(block))
        
        # deq = [source]
        
        rows = 10**6
        cols = 10**6
        
        def bfs(deq, targetd):
        
            for x, y in deq:

                if len(visit) == 20000:
                    return True

                if (x,y) in visit:
                    return

                visit.add((x,y))

                for i,j in [[-1,0],[1,0],[0,1],[0,-1]]:
                    nx, ny = x+i, y+j

                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visit and (nx, ny) not in blocked_set:
                        if [nx, ny] == targetd:
                            return True
                        deq.append((nx, ny))
                        visit.add((nx, ny))
                    
        return bfs([source], target) and bfs([target], source)
    
        """
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000: return True
            return False
        return bfs(source, target) and bfs(target, source)
        
        