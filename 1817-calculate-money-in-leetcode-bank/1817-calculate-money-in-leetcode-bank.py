class Solution:
    def totalMoney(self, n: int) -> int:
        c,k=0,1
        while n>0:
            for i in range(min(n,7)):
                c+=k+i
            n-=7
            k+=1
        return c