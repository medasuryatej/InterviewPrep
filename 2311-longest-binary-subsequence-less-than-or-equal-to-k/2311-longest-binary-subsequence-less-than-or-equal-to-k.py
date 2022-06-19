class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # keeping track current sum achieved from string formation
        curSum = 0
        # pointer to keep track of bit position
        pointer = 0
        # iterate from end position
        for bit in s[::-1]:
            # it bit is zero consider it, since it is allowed to have 
            # any number of leading zeros
            if bit == "0":
                # increment the pointer
                pointer += 1
            else:
                # if the bit is one, obtain how much value it would 
                # add to the curSum
                curValue = 2**pointer
                # if the newsum doesn't exceed k value, the bit one can 
                # be considered, else ignore
                if curSum + curValue <= k:
                    curSum += curValue
                    pointer += 1
        # return the current pointer position.
        return pointer