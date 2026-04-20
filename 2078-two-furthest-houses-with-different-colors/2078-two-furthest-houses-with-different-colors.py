class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0#                                          i     j
        for i in range(len(colors)):#                   0 1 2 3 4 5 6  
            for j in range(i+1,len(colors)): #colors = [1,1,1,6,1,1,1]
                if colors[i]!=colors[j]: # 1!=1, 1!=1,  1!=6
                    ans = max(ans,j-i) # 3-0
        return ans