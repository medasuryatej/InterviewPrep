class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numStr = str(num)
        count = 0
        
        for i in range(0, len(numStr) - k + 1, 1):
            subStr = int(numStr[i:i+k])
            if subStr == 0 or num % subStr != 0:
                continue
            count += 1
        
        return count