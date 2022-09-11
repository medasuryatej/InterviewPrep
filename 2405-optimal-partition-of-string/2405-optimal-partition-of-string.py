class Solution:
    def partitionString(self, s: str) -> int:
        # Have a set to keep track of visited characters
        seen_set = set()
        # initialize numParts
        numparts = 1
        # traverse through the characters
        for eachChar in s:
            # if the current character is already seen, then we need
            # to begin a new partition
            if eachChar in seen_set:
                numparts += 1
                seen_set = set()
            # mark the character as visited
            seen_set.add(eachChar)
            
        # return numberparts
        return numparts