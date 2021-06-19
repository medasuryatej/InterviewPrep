class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if k == 10:
            return sum([ int(val) for val in str(n) ])
        else:
            # remainders = list(range(10))
            output = []
            while n > 0:
                div, n = divmod(n, k)
                output.insert(0,n)
                n = div
            return sum(output)