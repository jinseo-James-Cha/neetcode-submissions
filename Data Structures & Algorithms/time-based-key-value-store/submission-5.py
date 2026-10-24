from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    # All the timestamps of set are strictly increasing.
    # insert after upper bound binary search
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        curr = self.timeMap[key]
        left = 0
        right = len(curr)
        while left < right:
            mid = (left + right) // 2
            if curr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        if left == 0:
            return ""
            
        return curr[left-1][1]


    # TLE
    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.timeMap:
    #         return ""
        
    #     res = ""
    #     max_time = -1
    #     for t, v in self.timeMap[key]:
    #         if t > timestamp:
    #             continue
            
    #         if t <= timestamp and abs(timestamp - max_time) > abs(timestamp - t):
    #             res = v
    #     return res


