class Solution(object):
    def countCompleteSubarrays(self, nums):
        k = len(set(nums))
        res = 0
        for i in range(len(nums)):
            st = set()
            for j in range(i, len(nums)):
                st.add(nums[j])
                if len(st) == k:
                    res += 1
        return res