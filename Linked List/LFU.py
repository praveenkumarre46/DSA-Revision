from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {} 
        self.freq_map = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update(self, key, value=None):
        val, freq = self.values[key]
        if value is not None:
            val = value
        
        self.freq_map[freq].pop(key)
        
        if not self.freq_map[self.min_freq] and self.min_freq == freq:
            self.min_freq += 1
            
        new_freq = freq + 1
        self.values[key] = [val, new_freq]
        self.freq_map[new_freq][key] = None
        return val

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        return self._update(key)

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.values:
            self._update(key, value)
            return

        if len(self.values) >= self.capacity:
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.values[evict_key]

        self.values[key] = [value, 1]
        self.freq_map[1][key] = None
        self.min_freq = 1