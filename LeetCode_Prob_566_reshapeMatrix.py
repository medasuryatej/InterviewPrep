class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # base Case
        if len(mat) * len(mat[0]) != r*c:
            # shape of mat and reshape matrix didn't match
            return mat
        temp = []
        for array in mat:
            temp.extend(array)
        reshape = []
        counter = 0
        for row in range(r):
            reshape.append(temp[counter:counter+c])
            counter += c
        return reshape
                