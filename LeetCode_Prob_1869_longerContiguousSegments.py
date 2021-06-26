def checkZeroOnes(s):
        maxOnes = 0
        maxZeros = 0
        # iterate over all chars
        # if char is 1:
        #   increment one count
        #   update maxZeros to max of prev or current streak
        #   reset zero count to zero
        # else:
        #  increment zero count
        #  update maxOnes to max of prev or current streak
        #  reset one count to zero
        oneCount, zeroCount = 0,0
        for char in s:
            if char == "1":
                oneCount += 1
                if zeroCount != 0:
                    maxZeros = max(maxZeros, zeroCount)
                    zeroCount = 0
            else:
                zeroCount += 1
                if oneCount != 0:
                    maxOnes = max(maxOnes, oneCount)
                    oneCount = 0
        maxZeros = max(maxZeros, zeroCount)
        maxOnes = max(maxOnes, oneCount)
        print(maxOnes, maxZeros)
        return maxOnes > maxZeros

s = "1101"
print(checkZeroOnes(s))

s = "111000"
print(checkZeroOnes(s))

s = "110100010"
print(checkZeroOnes(s))