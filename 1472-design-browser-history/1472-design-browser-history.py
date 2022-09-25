class DLL:
    def __init__(self, nodeVal):
        self.nodeVal = nodeVal
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll = DLL(homepage)
        # return self.dll.nodeVal
        

    def visit(self, url: str) -> None:
        newNode = DLL(url)
        self.dll.next = newNode
        newNode.prev = self.dll
        self.dll = self.dll.next
        # return self.dll.nodeVal
        

    def back(self, steps: int) -> str:
        while (steps and self.dll.prev):
            self.dll = self.dll.prev
            steps -= 1
        return self.dll.nodeVal
        

    def forward(self, steps: int) -> str:
        while (steps and self.dll.next):
            self.dll = self.dll.next
            steps -= 1
        return self.dll.nodeVal
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)