class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power2s = []
        start = 0
        while 2**start < 10**9:
            power2s.append("".join(sorted(str(2**start))))
            start += 1
        return "".join(sorted(str(n))) in power2s