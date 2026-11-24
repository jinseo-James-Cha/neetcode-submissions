import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        K closest to the points 0,0
        Euclidean distance = sqrt((x1 - x2) ^ 2 + (y1 - y2)^2)
        """
        min_heap = []
        for x, y in points:
            euclidean_distance = float(math.sqrt((x - 0)**2 + (y - 0)**2))
            heapq.heappush(min_heap, (euclidean_distance, x, y))
        
        res = []
        while len(res) < k:
            e_d, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        
        return res