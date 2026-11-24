import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        two heaviest stones
        if x == y -> both remove
        if x < y -> add y - x

        max heap
        """
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) >= 2:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y:
                continue
            
            if abs(x - y) > 0:
                heapq.heappush(max_heap, -abs(x-y))
        
        return 0 if not max_heap else -max_heap[0]