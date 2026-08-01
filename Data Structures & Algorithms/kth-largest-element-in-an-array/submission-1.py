import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # bucket sort
        min_num = min(nums)
        max_num = max(nums)
        bucket = [0] * (max_num - min_num + 1) # 5 - 1

        for num in nums:
            bucket[num - min_num] += 1
        
        for i in range(len(bucket)-1, -1, -1):
            k -= bucket[i]
            if k <= 0:
                return i + min_num
        return -1


        
        # min heap
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)
        return queue[0]