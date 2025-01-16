class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m,n=len(nums1),len(nums2)
        d={}
        for i in nums1:
            d[i]=d.get(i,0)+n
        for i in nums2:
            d[i]=d.get(i,0)+m
        ans=0
        for i in d:
            if d[i]%2:
                ans^=i
        return ans