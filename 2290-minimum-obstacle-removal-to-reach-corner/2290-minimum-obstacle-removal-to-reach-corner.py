class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # get rows and cols information
        rows, cols = len(grid), len(grid[0])
        # a set to keep track of visited elements
        visited = set()
        # a deq to traverse / bfs
        deq = [(0, (0, 0))] # (obstacles_removed, x_cord, y_cord)
        # four directions
        directions  = ([1, 0], [-1, 0], [0, 1], [0, -1])
        # while deq is not empty perform bfs
        while deq:
            # fetch the min
            minObstRem, (x, y) = heappop(deq) # pops that coords with minimum value in first coordinate i.e, minObstRem
            # check if node already visited
            if (x, y) in visited:
                # skip
                continue
            # add it to the visited set
            visited.add((x, y))
            # check if we reached destination
            if (x, y) == (rows-1, cols-1):
                # return the minimum number of obstacles removed
                return minObstRem
            # traverse all four directions
            for i, j in directions:
                # update coords
                new_x, new_y = x + i, y + j
                # check the boundaries and visit set
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                    # add the new coord to the heapify dep
                    # note grid[new_x][new_y] => if obstacle then it adds 1 to the minObstRem else 0
                    heappush(deq, (grid[new_x][new_y] + minObstRem, (new_x, new_y)))
        # unreachable
        return -1
            