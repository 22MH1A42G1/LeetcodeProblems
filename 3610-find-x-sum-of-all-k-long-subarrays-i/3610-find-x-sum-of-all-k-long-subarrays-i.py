from collections import Counter
from typing import List
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            s = nums[i:i + k]
            f = Counter(s)
            m = sorted(f.items(), key=lambda item: (-item[1], -item[0]))
            xs = sum(value * count for value, count in m[:x])
            ans.append(xs)
        return ans