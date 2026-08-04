class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = x^y
        c=0
        while d!=0:
            d&=d-1
            c+=1
        return c