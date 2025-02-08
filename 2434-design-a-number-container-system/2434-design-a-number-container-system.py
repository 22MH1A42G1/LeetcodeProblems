class NumberContainers:

    def __init__(self):
        self.indexToNum = {}
        self.numToIndices = {}

    def change(self, index: int, number: int) -> None:
        self.indexToNum[index] = number
        if number not in self.numToIndices:
            self.numToIndices[number] = []
        heapq.heappush(self.numToIndices[number], index)

    def find(self, number: int) -> int:
        if number not in self.numToIndices:
            return -1
        pq = self.numToIndices[number]        
        while pq:
            currIndex = pq[0]
            if self.indexToNum[currIndex] != number:
                heapq.heappop(pq)
            else:
                return currIndex
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

"""
- number -> heap of indices
- index -> value at that index (to validate)
"""