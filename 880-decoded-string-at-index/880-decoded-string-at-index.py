class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        N = 0
        for index, char in enumerate(s):
            if char.isalpha():
                N += 1
            else:
                N *= int(char)
            if k <= N:
                break
        for i in range(index, -1, -1):
            
            if s[i].isalpha():
                if k == 0 or k == N:
                    return s[i]
                N -= 1
            else:
                N /= int(s[i])
                k = k % N
                