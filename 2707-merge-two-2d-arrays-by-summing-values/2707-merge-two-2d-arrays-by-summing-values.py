class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        s = {}
        for i in nums1:
            s[i[0]]=i[1]
        #print(s)
        for i in nums2:
            s[i[0]]=s.get(i[0],0)+i[1]
        #print(s)
        l1=[]
        for i,j in sorted(s.items()):
            l1.append([i,j])
        return l1