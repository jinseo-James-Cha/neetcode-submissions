from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        key val timestamp
        """
        self.hashmap[key].append((timestamp, value))
        self.hashmap[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        """
        get a value key == key and timestamp_prev <= timestamp
        """
        if key not in self.hashmap:
            return ""
        
        found_list = self.hashmap[key]
        for t, v in found_list[::-1]:
            if t <= timestamp:
                return v
        return ""
