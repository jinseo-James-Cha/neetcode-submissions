import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # bucket sort
        min_num = min(nums)
        max_num = max(nums)
        buckets = [0] * (max_num - min_num + 1)
        for num in nums:
            buckets[num - min_num] += 1
        
        for i in range(len(buckets) - 1, -1, -1):
            k -= buckets[i]
            if k <= 0:
                return i + min_num
        return -1


        
        # max_heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        while k - 1 > 0:
            heapq.heappop(max_heap)
            k -= 1
        
        return -max_heap[0]