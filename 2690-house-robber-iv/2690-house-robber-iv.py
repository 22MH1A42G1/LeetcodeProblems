class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l,r,n=0,10**12,len(nums)
        def fun(t):
            c,i=0,0
            while i<n:
                if nums[i]<=t:
                    i+=2
                    c+=1
                    continue
                i+=1
            return c>=k
        while l<r:
            m=(l+r)//2
            if fun(m):
                r=m
            else:
                l=m+1
        return l
