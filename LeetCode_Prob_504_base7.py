class Solution:
    def convertToBase7(self, num: int) -> str:
        output = []
        val = abs(num)
        while val > 0:
            div, val = divmod(val, 7)
            output.insert(0, str(val))
            val = div
        return "-"*(num<0)  + "".join(output) or "0"