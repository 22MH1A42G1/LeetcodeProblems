class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        sign = (1 if s[0] != '-' else -1)
        s = (s[1:] if s[0] in ('-', '+') else s)
        result = 0
        for i in s:
            if not i.isdigit():break
            result = result * 10 + int(i)
        return max(min(result * sign, 2**31 - 1), -2**31)