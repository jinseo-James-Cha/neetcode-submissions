import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.pq = nums
        heapq.heapify(self.pq)
        while len(self.pq) > self.kth:
            heapq.heappop(self.pq)
    
    def add(self, val):
        heapq.heappush(self.pq, val)
        while len(self.pq) > self.kth:
            heapq.heappop(self.pq)
        return self.pq[0]