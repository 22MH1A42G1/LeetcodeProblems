class Solution:
    def sumAndMultiply(self, n: int) -> int:
        non_zero_digits = [int(digit) for digit in str(n) if digit != '0']
        if not non_zero_digits:
            return 0
        num_from_digits = int("".join(map(str, non_zero_digits)))
        return num_from_digits * sum(non_zero_digits)