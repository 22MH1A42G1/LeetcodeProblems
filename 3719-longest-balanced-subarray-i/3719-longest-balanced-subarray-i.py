class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ml = 0
        for r in range(0, len(nums)):
            o = set()
            e = set()
            for l in range(r, len(nums)):
                if nums[l]%2&1:
                    o.add(nums[l])
                else:
                    e.add(nums[l])
                if len(o)==len(e):
                    ml = max(ml, l-r+1)
        return ml