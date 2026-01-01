class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            c=0
            for j in range(n):
                if nums[j]<nums[i]:
                    c+=1
            ans.append(c)
        return ans