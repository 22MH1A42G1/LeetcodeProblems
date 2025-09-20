class Router:
    def __init__(self, memoryLimit: int):
        self.maxL = memoryLimit
        self.size = 0
        self.q = deque()
        #for keeping the track of packets to identify the duplicates
        self.packetCache = defaultdict(int)
        #for keeping the track of timestamps of destinations for using in the getCount method
        self.entries = defaultdict(deque)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) not in self.packetCache:
            self.q.append((source,destination,timestamp))
            self.packetCache[(source,destination,timestamp)]+=1
            self.entries[destination].append(timestamp)
            self.size+=1
            #if size exceeds the limit, after adding the new entry remove the packet from the start
            if self.size>self.maxL:
                firstPacket = self.q.popleft()
                self.packetCache[firstPacket]-=1
                if self.packetCache[firstPacket]==0:
                    del self.packetCache[firstPacket]
                    self.entries[firstPacket[1]].popleft()
                self.size-=1
            return True
        return False
        
        
    def forwardPacket(self) -> List[int]:
        if self.size>0:
            self.size-=1
            firstPacket= self.q.popleft()
            self.packetCache[firstPacket]-=1
            if self.packetCache[firstPacket]==0:
                del self.packetCache[firstPacket]
                self.entries[firstPacket[1]].popleft()
            return firstPacket
        return []
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect_left(self.entries[destination],startTime)
        right = bisect_right(self.entries[destination],endTime)
        # print(self.entries,left,right)
        #right-left gives the count of destinations within range of startTime and endtime
        return right-left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)