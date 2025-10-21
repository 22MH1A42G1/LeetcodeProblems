from bisect import bisect_left
from bisect import bisect_right
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        maxFreq = 0
        counter = Counter(nums)
        for i in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, i - k)
            right = bisect_right(nums, i + k) - 1
            maxFreq = max(maxFreq, min(right - left + 1, counter[i] + numOperations))
        return maxFreq