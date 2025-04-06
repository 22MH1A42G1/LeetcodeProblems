class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        c = [1] * n
        p = [-1] * n
        m = 0
        ind = -1
        nums.sort()
        if len(nums) ==1:
            return nums
        for i, k in enumerate(nums):
            for j in range(i):
                if k % nums[j] == 0 and c[i] < c[j] + 1:
                    c[i] = c[j] + 1
                    p[i] = j
                if c[i] > m:
                    m = c[i]
                    ind = i
        while ind != -1:
            ans.append(nums[ind])
            ind = p[ind]
        return ans
