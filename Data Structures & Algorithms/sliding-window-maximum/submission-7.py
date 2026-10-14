import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        window size = k

        return a maximum in each window

        1 2 1 0 4 2 6
        - - -           2
          - - -         2 2
            - - -       2 2 4
              - - -     2 2 4 4
                - - -   2 2 4 4 6
        """
        # Sliding window + deque
        # 1,2,1,0,4,2,6
        # 0 1 2 3 4 5 6
        #   L
        #         R
        # deque = 4
        res = [] # 2 2
        pq = deque()
        left = right = 0

        while right < len(nums):
            while pq and nums[pq[-1]] < nums[right]:
                pq.pop()
            pq.append(right)

            if left > pq[0]:
                pq.popleft()
            
            if right + 1 >= k:
                res.append(nums[pq[0]])
                left += 1
            right += 1
        return res


        # Max Heap -> O(n log n)
        max_heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
        return res


        # Brute force 2 -> TLE -> O(n * k)
        window = deque(nums[ :k])
        res = [max(window)]

        for right in range(k, len(nums)):
            window.popleft()
            window.append(nums[right])
            res.append(max(window))
        
        return res


        # Brute force -> O(n * k)
        output = []

        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            output.append(maxi)

        return output