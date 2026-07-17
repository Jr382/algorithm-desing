class Solution:
    min_int = -2147483648
    max_int = 2147483647
    def divide(self, dividend: int, divisor: int) -> int:
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        sign = (dividend == abs_dividend) ^ (divisor == abs_divisor)
        result = 0
        while abs_dividend >= abs_divisor:
            div = abs_divisor
            res = 1
            while div << 1 <= abs_dividend:
                div <<= 1
                res <<= 1
            abs_dividend -= div
            result += res

        return max(min(-result if sign else result, self.max_int), self.min_int)