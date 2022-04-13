class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        counter = 1
        n = rows = len(matrix)
        m = cols = len(matrix[0])
        row_start = 0
        row_end = n-1
        col_start = 0
        col_end = m-1
        while counter <= n*m:
            # go right
            for c in range(col_start, col_end+1):
                # result[row_start][c] = counter
                result.append(matrix[row_start][c])
                counter += 1
                
            # go down
            for r in range(row_start+1, row_end+1):
                # result[r][col_end] = counter
                result.append(matrix[r][col_end])
                counter += 1
            
            # go left
            if row_start != row_end:
                for c in reversed(range(col_start, col_end)):
                    # result[r][c] = counter
                    result.append(matrix[r][c])
                    counter += 1
                
            # go up
            if col_start != col_end:
                for r in reversed(range(row_start+1, row_end)):
                    # result[r][c] = counter
                    result.append(matrix[r][c])
                    counter += 1
                
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
            
        print(counter)
        return result