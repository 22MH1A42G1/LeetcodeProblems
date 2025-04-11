class Solution:
    def countSymmetricIntegers(self, l: int, h: int) -> int:
        return sum(sum(map(int,s[:q//2]))==sum(map(int,s[q//2:])) for v in range(l,h+1) if (q:=len(s:=str(v)))&1<1)