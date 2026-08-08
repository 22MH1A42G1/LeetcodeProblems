class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        c = [(sum(r),i) for i,r in enumerate(mat)]
        c.sort(key=lambda x: (x[0],x[1]))
        ans = []
        for i, j in c[:k]:
            ans.append(j)
        return ans