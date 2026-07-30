class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c =0
        l=0
        r=len(nums)-1
        while l< r:
            if nums[l]+nums[r]<target:
                c+=r-l
                l+=1
            else:
                r-=1
        return c