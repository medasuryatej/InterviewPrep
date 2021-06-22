class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap = {}
        for i in range(0, len(s) - 9):
            if s[i:i+10] in hashMap:
                hashMap[s[i:i+10]] += 1
            else:
                hashMap[s[i:i+10]] = 1
        output = set()
        for key, value in hashMap.items():
            if value > 1:
                output.add(key)
        return output