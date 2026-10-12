import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        sorted integer array
        k closest integers to x, in ascending order

        a closer than b
        |a - x| < |b - x|
        |a - x| == |b - x| and a < b

        distance between nums[i] and x 
        if distance is the same -> smaller integers

        - brute force
        - max heap by distance and arr[i]
        - sliding window
        """
        if len(arr) == k:
            return arr

        max_heap = []
        for num in arr:
            heapq.heappush(max_heap, (-abs(x - num), -num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return sorted([-num for dist, num in max_heap])

