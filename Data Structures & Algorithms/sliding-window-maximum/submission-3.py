from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Sliding window + deque
        res = []
        queue = deque()
        left = 0
        right = 0
        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if queue[0] < left:
                queue.popleft()
            
            if (right + 1) >= k:
                res.append(nums[queue[0]])
                left += 1
            right += 1
        return res



        
        # Heap
        pq = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            
            if i >= k - 1: # 2 >= 2 - 1
                while pq[0][1] <= i - k: # 0, 1 <= 2-2
                    heapq.heappop(pq)
                res.append(-pq[0][0])
        return res

        
        # Brute force
        res = []

        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            res.append(maxi)
        return res