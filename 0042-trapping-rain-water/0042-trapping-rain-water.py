class Solution:
    def trap(self, height: List[int]) -> int:
        lm = height[0]
        rm = height[-1]
        n = len(height)

        l=1
        r=n-2
        
        if n<=2:
            return 0
        
        w=0
        while l<=r:
            if lm<=rm:
                w+=max(0,min(lm,rm)-height[l])
                lm=max(lm,height[l])
                l+=1
            else:
                w+=max(0,min(lm,rm)-height[r])
                rm=max(rm,height[r])
                r-=1
        return w