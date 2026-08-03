from collections import deque
import heapq
class MedianFinder:

    def __init__(self):
        self.first_half_max_heap = []
        self.second_half_min_heap = []
        self.total_len = 0

    def addNum(self, num: int) -> None:
        self.total_len += 1

        heapq.heappush(self.first_half_max_heap, -num)

        if len(self.first_half_max_heap) - len(self.second_half_min_heap) >= 2:
            max_num = -heapq.heappop(self.first_half_max_heap)
            heapq.heappush(self.second_half_min_heap, max_num)
        
        max_in_first_half = -self.first_half_max_heap[0]
        min_in_second_half = self.second_half_min_heap[0] if self.second_half_min_heap else float('inf')
        if max_in_first_half > min_in_second_half:
            heapq.heappop(self.first_half_max_heap)
            heapq.heappop(self.second_half_min_heap)

            heapq.heappush(self.first_half_max_heap, -min_in_second_half)
            heapq.heappush(self.second_half_min_heap, max_in_first_half)

    def findMedian(self) -> float:
        print(self.first_half_max_heap)
        print(self.second_half_min_heap)
        if self.total_len % 2 != 0:
            return float(-self.first_half_max_heap[0])
        
        return float((-self.first_half_max_heap[0] + self.second_half_min_heap[0]) / 2)
        

        
        