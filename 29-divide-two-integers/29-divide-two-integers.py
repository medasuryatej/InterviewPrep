class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == 1 << 31 and divisor == -1): return 1>>31
        sign = (dividend >= 0) == (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while (dividend - divisor >= 0):
            count = 0
            while (dividend - (divisor << 1 << count) >= 0):
                count += 1
            result += 1 << count
            dividend -= divisor << count
        return min(result , 2**31 - 1) if sign else -result