class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(floor(Counter(s)[letter]/len(s) * 100))