class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lStack = []
        rStack = []
        for char in s:
            if char == "#" and lStack:
                lStack.pop()
            else:
                if char == "#":
                    continue
                lStack.append(char)
                
        for char in t:
            if char == "#" and rStack:
                rStack.pop()
            else:
                if char == "#":
                    continue
                rStack.append(char)
        # print(lStack)
        # print(rStack)
        return lStack == rStack