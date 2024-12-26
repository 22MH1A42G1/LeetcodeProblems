class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = sum(nums)
        m = [[float("-inf")] * (2*t+1) for _ in range(len(nums))]
        def f(nums,ci,cs,target,m):
            if ci==len(nums):
                return 1 if cs == target else 0
            else:
                if m[ci][cs+t] != float("-inf"):
                    return m[ci][cs+t]
                a = f(nums,ci+1,cs+nums[ci],target,m)
                s = f(nums,ci+1,cs-nums[ci],target,m)
                m[ci][cs+t]=a+s
                return m[ci][cs+t]
        return f(nums,0,0,target,m)