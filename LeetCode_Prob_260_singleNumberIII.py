class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        # xor funciton helps in getting rid of duplicates
        # Ex: 1 ^ 1 = 0
        for num in nums: 
            xor ^= num
        # currently xor variable has information of x, y in x^y format
        # the way we can determine these x and y are below
        # from the result x^y determine the first position where the binary 
        # representation of digits differed
        ## for example if given 
        """
            nums = [1,2,1,3,2,5]
            xor of every value returns 6
            binary representation of 6 is 110
            we see that the first difference comes in second position from left.
            so among  the two unique numbers one number must have its second position as 1,
            and the other as 0 => only then their xor product would result as 1 in the x^y
        """
        xor = xor & (xor - 1) ^ xor # returns the first character of difference
        a = b = 0
        for num in nums:
            if xor & num: # if a position contains 1 consider that as the number
                a ^= num  # any way when a duplicate is encountered that duplicate of xor results zero
            else:
                b ^= num
        return [a, b]