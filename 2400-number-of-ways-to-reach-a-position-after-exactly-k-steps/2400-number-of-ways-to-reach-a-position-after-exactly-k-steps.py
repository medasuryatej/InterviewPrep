from math import comb
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        distance_between_points = abs(endPos - startPos)
        # right_moves + left_moves = k
        # right_moves - left_moves = distance_between_points
        # right_moves = (k + distance_between_points) // 2
        
        # combinations
        # out of right + left options, we can choose right & left combinations
        
        right_moves = (k + distance_between_points) // 2
        
        left_moves = k - right_moves
        
        if left_moves < 0:
            return 0
        
        if distance_between_points % 2 != k % 2:
            return 0
        
        return comb(right_moves + left_moves, right_moves) % (10**9 + 7)