class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i]==target:
                ans.append(i)
        return ans