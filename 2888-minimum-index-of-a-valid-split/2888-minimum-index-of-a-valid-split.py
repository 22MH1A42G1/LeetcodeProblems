class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        l = 0
        d, r = max(Counter(nums).items(), key=lambda x: x[1])
        for i, x in enumerate(nums):
            l += x == d
            r -= x == d
            if l > (i + 1) // 2 and r > (len(nums) - (i + 1)) // 2:
                return i
        return -1