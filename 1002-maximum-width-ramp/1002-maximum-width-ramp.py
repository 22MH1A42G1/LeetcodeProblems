class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        s = []
        for i in range(n):
            if not s or nums[s[-1]]>nums[i]:
                s.append(i)
        m = 0
        for j in range(n-1,-1,-1):
            while s and nums[s[-1]]<=nums[j]:
                m = max(m,j-s.pop())
        return m