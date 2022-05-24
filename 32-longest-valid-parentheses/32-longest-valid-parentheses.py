class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0
        for index, each in enumerate(s):
            if each == "(":
                stack.append(index)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(index)
                else:
                    maxLen = max(maxLen, index - stack[-1])
        return maxLen