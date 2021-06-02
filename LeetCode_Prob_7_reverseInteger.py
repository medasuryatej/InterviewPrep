class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            value = int(str(x)[::-1].lstrip("0"))
            if value > (2**31 - 1):
                return 0
            else:
                return value
        elif x < 0:
            value = int(str(abs(x))[::-1].lstrip("0")) * -1
            if value < -2**31:
                return 0
            else:
                return value
        else:
            return 0