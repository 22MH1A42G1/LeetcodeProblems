class Solution:
    def addDigits(self, num: int) -> int:
        c = 0 
        while num > 0:
            c += num%10
            num //= 10
        return  c if c < 10 else self.addDigits(c)