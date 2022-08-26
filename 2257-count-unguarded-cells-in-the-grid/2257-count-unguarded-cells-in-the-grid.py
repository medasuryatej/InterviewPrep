class Solution:
    def countUnguarded_DFS(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        for x, y in guards+walls:
            dp[x][y] = 1
               
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for x, y in guards:
            for dx, dy in directions:
                curr_x = x
                curr_y = y
                
                while 0 <= curr_x+dx < m and 0 <= curr_y+dy < n and dp[curr_x+dx][curr_y+dy] != 1:
                    curr_x += dx
                    curr_y += dy
                    dp[curr_x][curr_y] = 2
                    
        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)
    
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
            '''## Approach : BFS ##'''
            rows , cols = m , n
            directions  = [(0,1),(0,-1),(1,0),(-1,0)]
            
            ## for efficiently search walls and gates
            wallsAndGuards = set()
            for r,c in walls+guards :
                wallsAndGuards.add((r,c))
            
            queue = deque()
            for r,c in guards :
                for dr,dc in directions :   # go to all the directions for the curr guard
                    queue.append([r,c,dr,dc])
                    
            visited = set()
            while queue :
                r,c,dr,dc = queue.popleft()
                visited.add((r,c))  
                newR, newC = r+dr, c+dc
                if newR<0 or newR>rows-1 or newC<0 or newC>cols-1 or (newR,newC) in wallsAndGuards:
                    continue
                queue.append( [newR,newC,dr,dc] )
            return m*n - len(visited) - len(walls)     # guard is already added in visitedSet