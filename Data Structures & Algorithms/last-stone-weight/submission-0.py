import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        queue = []
        for stone in stones:
            heapq.heappush(queue, -stone)


        while len(queue) > 1:
            y = -heapq.heappop(queue)
            x = -heapq.heappop(queue)

            if x < y:
                heapq.heappush(queue, -(y - x))
            
        return -queue[0] if len(queue) == 1 else 0