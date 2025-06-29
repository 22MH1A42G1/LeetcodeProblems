class Solution:
    def numSubseq(self, nums, target):
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod
                left += 1
            else:
                right -= 1

        return result