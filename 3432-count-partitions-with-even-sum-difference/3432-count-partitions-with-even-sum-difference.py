class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        t=sum(nums)
        l,r,c=0,0,0
        for i in range(len(nums)-1):
            l+=nums[i]
            r=t-l
            if (l-r)%2==0:
                c+=1
        return c