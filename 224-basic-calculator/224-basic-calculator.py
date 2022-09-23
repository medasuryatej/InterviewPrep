class Solution:
    def calculate(self, s: str) -> int:
        def updateSign(num, sign):
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
                
        pointer, number, stack, sign = 0, 0, [], "+"
        strLen = len(s)
        
        while pointer < strLen:
            curChar = s[pointer]
            
            if curChar.isnumeric():
                number = number * 10 + int(curChar)
                
            elif curChar in ("+", "-", "*", "/"):
                updateSign(number, sign)
                # update the new sign
                number, sign = 0, curChar
                
            elif curChar == "(":
                # recursive call
                number, offset = self.calculate(s[pointer + 1 :])
                pointer += offset
                
            elif curChar == ")":
                updateSign(number, sign)
                return sum(stack), pointer + 1
            
            pointer += 1
            
        updateSign(number, sign)
        
        return sum(stack)
                