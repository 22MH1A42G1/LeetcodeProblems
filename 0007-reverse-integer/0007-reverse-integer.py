class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        reverse = 0

        while x != 0:
            if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10)

        return reverse