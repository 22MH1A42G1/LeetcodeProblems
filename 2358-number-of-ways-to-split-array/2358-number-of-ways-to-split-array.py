class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l,r,c=0,sum(nums),0
        for i in range(len(nums)-1):
            l+=nums[i]
            r-=nums[i]
            if l>=r:
                c+=1
        return c