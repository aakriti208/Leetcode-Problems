# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item

# Time Complexity: O(1) for both get and put Space Complexity: O(capacity)


class LRUCache:
    def put(self, key):
        self.cache = list()
        

