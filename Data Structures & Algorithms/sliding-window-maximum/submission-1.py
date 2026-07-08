import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Heap
        pq = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            
            if i >= k - 1:
                while pq[0][1] <= i - k:
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