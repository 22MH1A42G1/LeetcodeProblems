class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        mp={}
        def dp(i,j):
            if i==len(nums1) or j==len(nums2): return float("-inf")
            if (i,j) in mp: return mp[(i,j)]
            p=nums1[i]*nums2[j]
            res = max(p+dp(i+1,j+1), p, dp(i+1,j), dp(i,j+1))
            mp[(i,j)]=res
            return mp[(i,j)]
        return dp(0,0)