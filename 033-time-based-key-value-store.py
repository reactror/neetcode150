class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        entries = self._map[key]
        if not len(entries): return ""
        
        l, r = 0, len(entries) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            entry = entries[m]
            
            if entry[1] == timestamp:
                return entry[0]
            elif entry[1] > timestamp:
                r = m - 1
            else:
                l = m + 1
                
        return entries[r][0] if r >= 0 else ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)