class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        c1,c2=0,0
        m,n=len(nums1),len(nums2)
        if n%2:
            for i in nums1:
                c1^=i
        if m%2:
            for i in nums2:
                c2^=i
        return c1^c2