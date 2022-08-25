class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)
        for char, freq in rCounter.items():
            if mCounter[char] < freq:
                return False
        return True