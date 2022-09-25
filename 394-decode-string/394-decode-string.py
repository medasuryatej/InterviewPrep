class Solution:
    def decodeString(self, s: str) -> str:
        stack, curNum, curString = [], 0, ""
        
        for char in s:
            # print(stack)
            if char == "[":
                # store the characters and number seen so far in the stack
                stack.extend([curString, curNum])
                # reset the num and string
                curNum, curString = 0, ""
            elif char == "]":
                # expand the strings
                multiplier = stack.pop()
                prevString = stack.pop()
                curString = prevString + curString * multiplier
            elif char.isdigit():
                curNum = curNum*10 + int(char)
            else:
                curString += char
            
        return curString
                
                