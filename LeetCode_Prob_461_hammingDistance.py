class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binX = bin(x)[2:]
        binY = bin(y)[2:]
        maxBits = max(len(binX), len(binY))
        binX = "0"*(maxBits - len(binX)) + binX
        binY = "0"*(maxBits - len(binY)) + binY
        counter = 0
        for _x, _y in zip(binX, binY):
            if _x != _y:
                counter += 1
        return counter
            
        