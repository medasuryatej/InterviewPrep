import math
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # transpose operation
        for i in range(num_rows):
            for j in range(i+1, num_cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # rotate
        for i in range(num_rows):
            for j in range(0, int(math.floor(num_cols/2))):
                matrix[i][j],matrix[i][num_cols-j-1] = matrix[i][num_cols-j-1],matrix[i][j]