class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left =0
        right = len(chars) -1
        while left < right:
            while left < right and not chars[left].isalpha():
                left += 1
            while right > left and not chars[right].isalpha():
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)