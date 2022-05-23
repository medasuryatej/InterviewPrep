class Solution:
    def grayCode(self, n: int) -> List[int]:
        prev = [0]
        current = [0]
        
        for i in range(1, n+1):
            addVal = (2 ** (i-1))
            while prev != []:
                # print(prev)
                top = prev.pop()
                current.append(top + addVal)
            prev = current.copy()
        return current