class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, s1, s2 = 1, 1, 1
        for a, b in pairwise(nums):
            if a > b:
                s2 += 1
                s1 = 1
            elif a < b:
                s1 += 1
                s2 = 1
            else:
                s2 = s1 = 1
            ans = max(s1, s2, ans)
        return ans