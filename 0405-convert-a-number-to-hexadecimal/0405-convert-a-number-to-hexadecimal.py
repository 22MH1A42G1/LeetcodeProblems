class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        if num < 0: num += 2**32
        return hex(num)[2:]