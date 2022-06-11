class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        
        def evaluate(a, b, op):
            print(f"Doing {b} {op} {a}")
            if op == "+":
                return b+a
            elif op == "-":
                return b-a
            elif op == "*":
                return b * a
            elif op == "/":
                return int(b / a)
            else:
                print("invalid op")
                return -1
        
        
        for token in tokens:
            if token in ops:
                top = stack.pop()
                next_top = stack.pop()
                result = evaluate(top, next_top, token)
                stack.append(result)
            else:
                stack.append(int(token))
                
        print(stack)
        return stack[0]