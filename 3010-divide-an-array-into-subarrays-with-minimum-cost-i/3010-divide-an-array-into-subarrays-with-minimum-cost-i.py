class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        nums1 = nums.copy()
        nums1.sort()
        f = nums1.pop(nums1.index(nums[0]))
        # print(nums,nums1)
        return nums[0]+nums1[0]+nums1[1]