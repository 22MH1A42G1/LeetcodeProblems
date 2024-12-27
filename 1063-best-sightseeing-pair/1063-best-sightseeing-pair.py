class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        mls=[0]*n
        mls[0]=values[0]
        ms=0
        for i in range(1,n):
            crs=values[i]-i
            ms=max(ms,mls[i-1]+crs)
            cls=values[i]+i
            mls[i]=max(mls[i-1],cls)
        return ms