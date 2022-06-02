class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # create a tp matrix of below format
        return zip(*matrix)