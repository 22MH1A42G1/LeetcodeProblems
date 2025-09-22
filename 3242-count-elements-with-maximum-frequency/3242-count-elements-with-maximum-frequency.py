class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        l = Counter(nums)
        m = max(l.values())
        c = sum([1 for i in nums if l[i] == m])
        return c