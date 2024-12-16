class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            i = 0
            ans = nums[0]
            for j in range(1, n):
                if nums[j] < ans:
                    ans = nums[j]
                    i = j
            nums[i] *= multiplier
        return nums