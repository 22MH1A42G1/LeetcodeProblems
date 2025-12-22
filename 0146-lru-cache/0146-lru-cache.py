class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_queue = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.lru_queue.pop(0)
                del self.cache[lru_key]
            self.cache[key] = value
            self.lru_queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
