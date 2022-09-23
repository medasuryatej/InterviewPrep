from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        c = Counter(chars)
        for word in words:
            w = Counter(word)
            cantUse = False
            for l, f in w.items():
                if f > c[l]:
                    cantUse = True
                    break
            if not cantUse:
                output += len(word)
                
        return output
                    