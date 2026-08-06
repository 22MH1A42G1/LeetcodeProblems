class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        sl = [int(i) for i in str(n)]
        print(sl)
        return x in sl and sl[0]!=x