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
        # binary search
        l, r = 0, len(arr) - k
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l + k]


        # binary search + two pointers
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        
        l, r = l - 1, l
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r]


        # two pointers
        left = 0
        right = len(arr) - 1
        while right - left >= k:
            if abs(x - arr[left]) <= abs(x - arr[right]):
                right -= 1
            else:
                left += 1
        return arr[left:right + 1]


        n = len(arr)
        idx = 0
        for i in range(1, n):
            if abs(x - arr[idx]) > abs(x - arr[i]):
                idx = i

        res = [arr[idx]]
        l, r = idx - 1, idx + 1

        while len(res) < k:
            if l >= 0 and r < n:
                if abs(x - arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1

        return sorted(res)


        # Max heap
        if len(arr) == k:
            return arr

        max_heap = []
        for num in arr:
            heapq.heappush(max_heap, (-abs(x - num), -num))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return sorted([-num for dist, num in max_heap])

