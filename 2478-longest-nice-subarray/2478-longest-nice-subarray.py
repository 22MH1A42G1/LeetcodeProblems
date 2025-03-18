class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        u = 0 
        s = 0
        m = 0 
        for e in range(len(nums)):
            while u & nums[e] != 0:
                u ^= nums[s]
                s += 1
            u |= nums[e]
            m = max(m, e - s + 1)
        return m