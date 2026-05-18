class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        base = list(range(1,len(nums)))+[len(nums)-1]
        # print(nums)
        # print(base)
        return nums == base