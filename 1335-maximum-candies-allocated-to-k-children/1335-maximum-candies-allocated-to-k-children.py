class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        c=0
        for i in candies: c=max(c,i)
        l,r=0,c
        def fun(c,k,i):
            m=0
            for p in c: m+=p//i
            return m>=k
        while l<r:
            m=(l+r+1)//2
            if fun(candies,k,m): l=m
            else: r=m-1
        return l