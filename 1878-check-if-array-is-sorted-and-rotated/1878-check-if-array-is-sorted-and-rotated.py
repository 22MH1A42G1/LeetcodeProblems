class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i:]+nums[:i]==sorted(nums):
                return True
        return False