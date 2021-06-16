def transpose(matrix):
        # create a tp matrix of below format
        return zip(*matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))