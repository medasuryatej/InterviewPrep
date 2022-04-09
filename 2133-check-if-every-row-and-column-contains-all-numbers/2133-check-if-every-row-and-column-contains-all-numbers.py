class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rng = len(matrix)
        comp_set = set([i for i in range(1, rng+1)])
        for row in matrix:
            if set(row) != comp_set:
                return False
        for col in zip(*matrix):
            if set(col) != comp_set:
                return False
        return True