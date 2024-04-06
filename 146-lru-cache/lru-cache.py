class LRUCache:

    # we want to implement LRU (least recently used) which evicts the least recently used entry. 
    # you would use this in a cache where recently used entries are most likely to be reused!

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]     

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)