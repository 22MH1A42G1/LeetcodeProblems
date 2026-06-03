class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        MAX = 300005
        l = w = minL = minW = MAX
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):
            l = min(l, landStartTime[i] + landDuration[i])

        for i in range(m):
            w = min(w, waterStartTime[i] + waterDuration[i])
            minL = min(minL, max(waterStartTime[i], l) + waterDuration[i])

        for i in range(n):
            minW = min(minW, max(landStartTime[i], w) + landDuration[i])

        return min(minW, minL)