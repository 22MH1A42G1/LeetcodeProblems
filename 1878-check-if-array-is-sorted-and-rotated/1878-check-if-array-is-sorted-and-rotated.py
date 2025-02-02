class Solution:
    def check(self, nums: List[int]) -> bool:
        return True if sum(nums[i:]+nums[:i]==sorted(nums) for i in range(len(nums))) else False