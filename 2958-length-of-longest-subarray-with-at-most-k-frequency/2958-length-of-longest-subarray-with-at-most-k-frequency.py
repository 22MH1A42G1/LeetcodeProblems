class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        C = Counter()
        s = ans = 0
        for i,n in enumerate(nums):
            C[n] += 1
            while C[n] > k:
                C[nums[s]] -= 1
                s += 1
            ans = max(ans, i-s)
        return ans+1  