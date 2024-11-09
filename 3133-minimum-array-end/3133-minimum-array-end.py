class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bit=1
        n -= 1
        while n:
            while x & bit: 
                bit*= 2 
            if n & 1:  
                x^= bit
            n//= 2 
            bit*= 2
        return x