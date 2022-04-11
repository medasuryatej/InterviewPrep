class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from itertools import chain
        total_size = len(grid) * len(grid[0])
        k = k % total_size
        unraveled = list(chain(*grid))
        shifted = unraveled[-1:-1-k:-1][::-1] + unraveled[:len(unraveled)-k]
        print(shifted)
        chunk_size = len(grid[0])
        # output = [shifted[i:i+len(grid[0])] for i in range(0, len(shifted), len(grid[0]))]
        output = [shifted[i: i + chunk_size] for i in range(0, len(shifted), chunk_size)]
        return output