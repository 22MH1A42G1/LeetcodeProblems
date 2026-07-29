class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        s = []
        m = -1
        r = -1
        for i, j in enumerate(mat):
            print(i,j)
            co = j.count(1)
            if co>m:
                m=co
                r=i
        return [r,m]