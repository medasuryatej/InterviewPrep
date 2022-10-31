class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        digs = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                digs[i-j].add(matrix[i][j])
                
        for each in digs:
            if len(digs[each]) > 1:
                return False
        return True