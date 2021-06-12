class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        strlen = len(s)
        for j in range(0, strlen//2):
            s[j], s[strlen-j-1] = s[strlen-j-1], s[j]