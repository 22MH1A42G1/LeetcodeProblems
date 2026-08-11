class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        t = nums[0]
        for a, b in pairwise(nums):
            if b == a + 1:
                t += b
            else:
                break
        n = set(nums)
        while t in n:
            t += 1
        return t