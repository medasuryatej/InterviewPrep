class Solution:
    def toHex(self, num: int) -> str:
        remainders = [ str(val) for val in range(10) ] + list("abcdef")
        output = []
        if num > 0:
            while num > 0:
                div, num = divmod(num, 16)
                output.insert(0, remainders[num])
                num = div
        elif num == 0:
            return "0"
        else:
            num += 2**32
            while num > 0:
                div, num = divmod(num, 16)
                output.insert(0, remainders[num])
                num = div
        return "".join(output)