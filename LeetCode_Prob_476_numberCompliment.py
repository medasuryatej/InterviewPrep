class Solution:
    def findComplement(self, num: int) -> int:
        comp = [ str(1^int(bit)) for bit in bin(num)[2:]]
        return int("".join(comp),2)