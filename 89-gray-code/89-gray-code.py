class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 1:
            return [0, 1]
        
        # create a map for every bit with a list of 2**n zeros
        bitPos = {i : [0] * (2 ** n) for i in range(n)}
        
        # for _ in bitPos:
        #    print(_, bitPos[_])
        
        # total bits
        totalBits = (2 ** n)
        
        # for every bit position
        for bit in bitPos:
            # based on bit number the number of consecutive ones differ
            numConsecTrues = (2 ** (bit+1))
            # starting position is 2**bit
            startingPos = (2 ** bit)
            # counter to keep track of number of consecutive ones
            counter = 0
            # left = 0
            # print(bit, startingPos, numConsecTrues)
            # update the ones
            while startingPos < totalBits:
                if counter == numConsecTrues:
                    startingPos += numConsecTrues
                    counter = 0
                else:
                    bitPos[bit][startingPos] = 1
                    counter += 1
                    startingPos += 1
                    
        # for _ in bitPos:
        #    print(_, bitPos[_])
                    
        output = []
        for bits in zip(*bitPos.values()):
            numTostr = list(map(str, bits))
            binRep = "".join(numTostr)
            output.append(int(binRep, 2))
            
        return output