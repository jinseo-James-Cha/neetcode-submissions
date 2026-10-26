class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # binary search
        length = mountainArr.length()
        left = 1
        right = length - 2
        while left <= right:
            mid = (left + right) // 2
            left_val = mountainArr.get(mid - 1)
            mid_val = mountainArr.get(mid)
            right_val = mountainArr.get(mid + 1)
            if left_val < mid_val < right_val:
                left = mid + 1
            elif left_val > mid_val > right_val:
                right = mid - 1
            else:
                break
        peak = mid

        # search left portion 0 ~ peak - 1
        left = 0
        right = peak - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return mid
        
        # search right portion peak ~ n - 1
        left = peak
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val > target:
                left = mid + 1
            elif val < target:
                right = mid - 1
            else:
                return mid
        return -1



        # Brute force
        n = mountainArr.length()

        for i in range(n):
            if mountainArr.get(i) == target:
                return i

        return -1