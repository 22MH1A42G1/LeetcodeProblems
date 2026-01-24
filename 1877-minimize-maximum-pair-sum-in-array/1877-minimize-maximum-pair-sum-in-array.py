class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        for i in range(len(nums)//2):
            m=max(m,nums[i]+nums[len(nums)-1-i])
        return m