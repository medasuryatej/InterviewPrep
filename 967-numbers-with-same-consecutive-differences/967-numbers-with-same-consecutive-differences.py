class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # referred solution
        if n == 1: return range(10)
        
        result = []
        
        @cache
        def dfs(numDigitsLeft, currentNum):
            if numDigitsLeft == 0:
                return result.append(currentNum)
                
            tailNumber = currentNum % 10
            
            possibleCombinations = set([tailNumber + k, tailNumber - k])
            
            for eachComb in possibleCombinations:
                # checking if the combination is in range [0,9]
                if 0 <= eachComb <= 9:
                    updatedNumber = currentNum * 10 + eachComb
                    dfs(numDigitsLeft - 1, updatedNumber)
                    
        # perform dfs for every starting input
        for i in range(1, 10):
            dfs(n-1, i)
            
        return result