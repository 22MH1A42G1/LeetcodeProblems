class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        b=0
        d={}
        for i in range(len(nums)):
            g=d.get(i-nums[i],0)
            b+=i-g
            d[i-nums[i]]=g+1
        return b