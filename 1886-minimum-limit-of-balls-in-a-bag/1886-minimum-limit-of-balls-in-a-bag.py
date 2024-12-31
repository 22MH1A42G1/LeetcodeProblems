class Solution:
    def minimumSize(self, nums: List[int], maxOps: int) -> int:
        low, high = 1, max(nums) # min and max posible bags
        while low < high:
            mid = (low + high) // 2
            if sum((n - 1) // mid for n in nums) <= maxOps: high = mid
            else: low = mid + 1
        return high