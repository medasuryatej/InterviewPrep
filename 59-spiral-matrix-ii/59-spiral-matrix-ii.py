class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for c in range(n)] for r in range(n)]
        counter = 1
        rows = n
        cols = n
        row_start = 0
        row_end = n-1
        col_start = 0
        col_end = n-1
        while counter <= n**2:
            # go right
            for c in range(col_start, col_end+1):
                result[row_start][c] = counter
                counter += 1
                
            # go down
            for r in range(row_start+1, row_end+1):
                result[r][col_end] = counter
                counter += 1
            
            # go left
            for c in reversed(range(col_start, col_end)):
                result[r][c] = counter
                counter += 1
                
            # go up
            for r in reversed(range(row_start+1, row_end)):
                result[r][c] = counter
                counter += 1
                
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
            
        print(counter)
        return result