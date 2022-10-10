class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        output = list(palindrome)
        if len(output) == 1:
            return ""
        changed = False
        for i in range(len(output)//2):
            if output[i] != "a":
                output[i] = "a"
                changed = True
                break
        if not changed:
            output[-1] = "b"
        return "".join(output)