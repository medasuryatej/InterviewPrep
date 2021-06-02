class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = min(strs)
        if len(minimum) == 0:
            return ""
        count = 0
        while count < len(minimum):
            c = minimum[count]
            matched = True
            for each in strs:
                if each[count] == c:
                    pass
                else:
                    matched = False
                    break
            if matched == False:
                return minimum[:count]
            else:
                count += 1
        return minimum[:count]