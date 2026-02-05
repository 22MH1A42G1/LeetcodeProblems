class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ms=0
        nums.sort()
        for i in range(0,len(nums),2):
            ms+=nums[i]
        return ms