class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        max_beauty = 0

        for i, num in enumerate(nums):
            upper_bound = self._find_upper_bound(nums, num + 2 * k)
            max_beauty = max(max_beauty, upper_bound - i + 1)

        return max_beauty

    def _find_upper_bound(self, arr: list[int], val: int) -> int:
        low, high, result = 0, len(arr) - 1, 0
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= val:
                result = mid 
                low = mid + 1
            else:
                high = mid - 1

        return result