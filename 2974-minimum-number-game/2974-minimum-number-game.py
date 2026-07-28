class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort() 
        ans = []
        for i in range(0,len(nums),2):
            ans.append(nums[i+1]) 
            ans.append(nums[i])
        return ans