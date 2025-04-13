class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(5,ceil(n/2),m:=10**9+7)*pow(4,n//2,m)%m