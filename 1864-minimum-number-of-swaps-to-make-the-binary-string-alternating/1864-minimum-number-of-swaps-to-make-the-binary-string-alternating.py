class Solution:
    def minSwaps(self, s: str) -> int:
        # if difference between num ones and zeros is more than 1 then ans is impossible
        # count for num1s
        #   # if num1s > num0s then answer must start with 1
        #   # elif num1s < num0s then answer must start with 0
        #   # else min (start with 1, start with 0)
        #   # we just find number of mismatches and answer is mimatches/2
        chars = list(map(int, list(s)))
        numOnes = sum(chars)
        numChars = len(chars)
        numZeros = numChars - numOnes
        
        if abs(numZeros - numOnes) > 1:
            return -1
        
        def getMinSwaps(chars, compare):
            count = 0
            # iterate over every char and
            # check if they are alternating or note
            for char in chars:
                if char != compare:
                    count += 1
                # switching the compare char to check if the digits 
                # are alternating or not
                if compare:
                    compare = 0
                else:
                    compare = 1
            return count
        
        if numOnes == numZeros:
            minSwaps = min(getMinSwaps(chars, 1), getMinSwaps(chars, 0))
        else:
            minSwaps = getMinSwaps(chars, 1 if numOnes > numZeros else 0)
            
        return minSwaps // 2