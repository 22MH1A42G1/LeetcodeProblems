class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
        meetings.sort()#[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
        a = [i for i in range(n)] #[0,1,2]
        u = []#(endTime,roomNo) -->[(10, 2), (20, 0), (12, 1)]
        c = [0]*n#[0,0,0] meetings schedule--->[1, 2, 2]
        for i,j in meetings: #[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]] in (len(i)=5,len(j)=2)
            while u and i>=u[0][0]:# [];[] 
                e,r=heapq.heappop(u)# end,room=pop(u)
                heapq.heappush(a,r)# a.push(r)
            if not a:#a==None
                et,r=heapq.heappop(u)# endTime,Room=pop(u)
                j=et+(j-i)#j=endTime+(j-i)
                heapq.heappush(a,r)#a.push(r)
            r=heapq.heappop(a)#r=a.pop()
            heapq.heappush(u,(j,r))#u.push(j,r)-->[(10, 2), (20, 0), (12, 1)]
            c[r]+=1 #[1, 2, 2]
        return c.index(max(c))#1