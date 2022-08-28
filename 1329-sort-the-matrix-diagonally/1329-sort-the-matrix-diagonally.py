class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[c-r].append(mat[r][c])
                
        for each in diagonals:
            diagonals[each].sort(reverse=True)
            
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat[r][c] = diagonals[c-r].pop()
            
        return mat
        