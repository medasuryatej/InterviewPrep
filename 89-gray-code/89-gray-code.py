class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        n = 1 output [0, 1]
        n = 2 output [00, 01, 11, 10 ]
        n = 3 output [000, 001, 011, 010, 110, 111, 101, 100]
        
        -------
        Half Zeros, One fourth Zeros,  --> next One eight and so on
                    One fourth Ones,
                       (flip the order)
        
        Half Ones   One fourth Ones,
                    One fourth Zeros
        
        The pattern continues.
        
        """
        
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
                    # increase the offset
                    startingPos += numConsecTrues
                    # reset the counter
                    counter = 0
                else:
                    # flip the bit by one
                    bitPos[bit][startingPos] = 1
                    # increment the counter
                    counter += 1
                    # increment the positon
                    startingPos += 1
                    
        # for _ in bitPos:
        #    print(_, bitPos[_])
                    
        output = []
        # merging the outputs
        for bits in zip(*bitPos.values()):
            # map the bits to string
            numTostr = list(map(str, bits))
            # join the string
            binRep = "".join(numTostr)
            # convert bin string to int
            output.append(int(binRep, 2))
            
        return output