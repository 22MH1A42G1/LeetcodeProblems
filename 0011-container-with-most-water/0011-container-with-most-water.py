class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        if n==0: return 0
        l=0
        r=n-1
        m=0
        c=0
        while l<r:
            c=min(height[l],height[r])*(r-l) 
            m=max(m,c) 
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return m