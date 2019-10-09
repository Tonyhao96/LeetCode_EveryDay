#146_LRU Cache
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Use OrderedDict
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._dict = OrderedDict()
        self._capacity=capacity

    def get(self, key: int) -> int:
        self._move_to_end_if_exist(key)
        return self._dict.get(key,-1)

    def put(self, key: int, value: int) -> None:
        self._move_to_end_if_exist(key)
        self._dict[key]=value
        if len(self._dict) > self._capacity:
            self._dict.popitem(last=False)
        
    def _move_to_end_if_exist(self, key: int):
        if key in self._dict:
            self._dict.move_to_end(key)



#Need Python 3.7 or higher
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity

    def get(self, key: int) -> int:
        value=self.cache.get(key,-1)
        if value!=-1:
            del self.cache[key]
            self.cache[key]=value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            del self.cache[next(iter(self.cache))]