class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            p=1
            j=i
            while j>0:
                p*=j%10
                j//=10
            if p%t==0:
                return i
        return -1