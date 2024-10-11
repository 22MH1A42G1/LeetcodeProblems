class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        o = sorted(range(len(times)),key=lambda x:times[x][0])
        e,t=list(range(len(times))), []
        for i in o:
            a,l=times[i]
            while t and t[0][0]<=a:
                heappush(e,heappop(t)[1])
            s = heappop(e)
            if i == targetFriend: return s
            heappush(t,(l,s))