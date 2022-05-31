class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        numCodes = 2 ** k
        allCodes = set()
        allCodes.add(s[:k])
        for i in range(1, len(s)-k+1):
            allCodes.add(s[i:i+k])
        # print(allCodes)
        return len(allCodes) >= numCodes