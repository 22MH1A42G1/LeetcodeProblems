class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        for i in range(len(nums)):
            l.append(sum(nums[:i]))
            r.append(sum(nums[i+1:]))
        # print(l,r)
        return [abs(i-j) for i,j in zip(l,r)]