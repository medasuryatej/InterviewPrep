class Solution:
    def divisorGame(self, n: int) -> bool:
        if n < 2:
            return False
        else:
            return n%2 == 0