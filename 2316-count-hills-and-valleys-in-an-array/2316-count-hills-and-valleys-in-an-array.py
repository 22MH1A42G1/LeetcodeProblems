class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        left = 0

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                if (nums[i] > nums[left] and nums[i] > nums[i + 1]) or \
                   (nums[i] < nums[left] and nums[i] < nums[i + 1]):
                    count += 1
                left = i

        return count