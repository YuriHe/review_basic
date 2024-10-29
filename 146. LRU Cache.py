class LRUCache:
    """
    Question: maintain LRU least recently used cache
    Use get&put T:O(1) -> think use hashmap, double linked list
    """
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {} # store key value pair
        self.order = [] # store key maximum size is capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # get is action
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update cache and order 
            self.order.remove(key)
        else:
            if len(self.cache)>= self.size: # before add
                # remove least use first from order
                pop = self.order.pop(0)
                # remove from cache
                self.cache.pop(pop)
            
        self.order.append(key)
        self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)