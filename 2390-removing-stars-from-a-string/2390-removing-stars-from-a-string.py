class Solution:
    def removeStars(self, s: str) -> str:
        result = ""
        for char in s:
            if char == "*":
                result = result.removesuffix(result[-1])
            else:
                result += char
        return result