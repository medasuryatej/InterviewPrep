class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        deq = [(0, 0, 0)]
        while deq:
            rem, x, y = heappop(deq)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            if (x, y) == (rows-1, cols-1):
                return rem
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_x, new_y = x+ i, y + j
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in seen:
                    heappush(deq, (grid[new_x][new_y] + rem, new_x, new_y))
        return rem
                    
            