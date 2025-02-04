class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum_num, max_sum = nums[0], nums[0]
        for a, b in pairwise(nums):
            if b > a:
                sum_num += b
            else:
                sum_num = b
            max_sum = max(sum_num, max_sum)
        return max_sum