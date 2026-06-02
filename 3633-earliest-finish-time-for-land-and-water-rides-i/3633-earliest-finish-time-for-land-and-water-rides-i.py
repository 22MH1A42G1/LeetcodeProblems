class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        r = float('inf')
        for i in range(n):
            for j in range(m):
                l = landStartTime[i]+landDuration[i]
                lw = max(l, waterStartTime[j])+waterDuration[j]
                r = min(r, lw)
                w = waterStartTime[j]+waterDuration[j]
                wl = max(w, landStartTime[i])+landDuration[i]
                r = min(r, wl)
        return r