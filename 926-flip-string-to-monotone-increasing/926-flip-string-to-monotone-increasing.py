class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # at any point of time keep track of num ones and numzeros
        # the minimum of these are the bits need to be flipped
        # to achieve monotonicity
        ones = 0
        zeros = 0
        for char in s:
            if char == "1":
                ones += 1
            else:
                zeros += 1
            zeros = min(zeros, ones)
        return zeros