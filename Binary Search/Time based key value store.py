class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.map=defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map[key]
        low, high = 0, len(values) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        
        return values[high][0] if high >= 0 else ""
