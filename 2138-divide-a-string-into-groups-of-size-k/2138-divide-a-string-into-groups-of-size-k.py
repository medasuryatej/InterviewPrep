class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for i in range(0, len(s), k):
            output.append(s[i:i+k])
        output[-1] = output[-1].ljust(k, fill)
        return output