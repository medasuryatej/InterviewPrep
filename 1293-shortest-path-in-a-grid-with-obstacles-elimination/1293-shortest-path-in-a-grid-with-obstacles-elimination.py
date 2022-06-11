from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows == cols == 1:
            return 0
        
        visited = set([(0, 0, k)])
        que = deque([(0, 0, k, 0)])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        if k > (rows + cols - 2):
            return rows + cols - 2
        
        while que:
            x, y, k_rem, steps = que.popleft()
            for i, j in directions:
                nx, ny = x+i, y+j
                if 0 <= nx < rows and 0 <= ny < cols:
                    # if obstacle and not visited
                    if grid[nx][ny] and k_rem and (nx, ny, k_rem-1) not in visited:
                        visited.add((nx, ny, k_rem-1))
                        que.append((nx, ny, k_rem-1, steps+1))
                    if grid[nx][ny] == 0 and (nx, ny, k_rem) not in visited:
                        # reached end
                        if nx == rows-1 and ny == cols-1:
                            return steps + 1
                        visited.add((nx, ny, k_rem))
                        que.append((nx, ny, k_rem, steps + 1))
        return -1