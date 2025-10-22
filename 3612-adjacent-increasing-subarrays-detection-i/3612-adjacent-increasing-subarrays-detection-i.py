class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        temp,c=0,1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                c+=1
            else:
                temp=c
                c=1
            if c // 2 >= k or temp//2 >= k or min(c,temp)>=k:
                return True
        return False

