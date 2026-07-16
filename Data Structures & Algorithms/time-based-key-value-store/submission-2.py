from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        key val timestamp
        timestamps are strictly increasing! 
        """
        self.hashmap[key].append((timestamp, value))

    # binary search upperbound - 1
    # 1 2 3
    # 4
    def get(self, key: str, timestamp: int) -> str:
        """
        get a value key == key and timestamp_prev <= timestamp
        """
        if key not in self.hashmap:
            return ""

        key_list = self.hashmap[key]    
        left = 0
        right = len(key_list)
    
        while left < right:
            mid = (left + right) // 2
            if key_list[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if left == 0 else key_list[left-1][1]
            




    # iterative from the back
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
