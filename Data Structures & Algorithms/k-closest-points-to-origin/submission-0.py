import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Calculate Euclidean distance and pop with heapq
        """

        queue = []
        min_x = 0
        min_y = 0
        for x, y in points:
            euclidean_distance = float(math.sqrt(x**2 + y**2))
            heapq.heappush(queue, (euclidean_distance, x, y))
        print(queue)
        res = []
        for _ in range(k):
            e_d, x, y = heapq.heappop(queue)
            res.append([x, y])
        return res