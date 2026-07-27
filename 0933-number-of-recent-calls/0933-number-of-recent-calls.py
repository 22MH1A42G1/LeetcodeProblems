class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.c = 0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[self.c]<t-3000:
            self.c+=1
        return len(self.queue)-self.c


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
