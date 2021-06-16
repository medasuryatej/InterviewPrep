class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        r = Counter(s)
        result = ""
        for key, value in r.most_common():
            result += key*value
        return result