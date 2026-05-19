class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = s1.intersection(s2)
        lc = -1
        if s3:
            lc=min(s3)
        return lc