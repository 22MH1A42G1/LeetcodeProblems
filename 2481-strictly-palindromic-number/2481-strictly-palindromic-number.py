import numpy as np
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def baseSwitch(i, n):
            res = ""
            while n != 0:
                res += str(n % i)
                n = n // i
            return res[::-1]
        for i in range(2, n-1):
            strBase = baseSwitch(i, n)
            if strBase != strBase[::-1]:
                return False
        return True