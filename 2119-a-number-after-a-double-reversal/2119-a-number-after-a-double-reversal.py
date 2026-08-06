class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = int(str(num)[::-1])
        s = int(str(n)[::-1])
        return s==num