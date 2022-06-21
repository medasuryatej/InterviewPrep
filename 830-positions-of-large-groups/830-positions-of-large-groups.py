class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        output = []
        counter = 1
        start = 0
        s += " "
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            else:
                if counter >= 3:
                    output.append([start, i-1])
                start = i
                counter = 1
        return output