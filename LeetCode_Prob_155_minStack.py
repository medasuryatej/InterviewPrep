class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minElement = None
        

    def push(self, val: int) -> None:
        # return self.stack.append(val)
        if not self.stack:
            self.stack.append(val)
            self.minElement = val
        else:
            if val < self.minElement:
                self.stack.append((2 * val) - self.minElement)
                self.minElement = val
            else:
                self.stack.append(val)
        

    def pop(self) -> None:
        # return self.stack.pop()
        if self.stack:
            value = self.stack.pop()
            if value < self.minElement:
                output = self.minElement
                self.minElement = (2 * self.minElement) - value
                return output
            else:
                return value
        else:
            return None
        

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1] if self.stack[-1] > self.minElement else self.minElement
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()