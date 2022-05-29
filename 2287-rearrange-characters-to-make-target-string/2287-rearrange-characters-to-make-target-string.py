class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(target)
        max_copies = float("inf")
        for char in t_counter:
            if char not in s_counter:
                return 0
            max_copies = min(s_counter[char] // t_counter[char], max_copies)
        return max_copies