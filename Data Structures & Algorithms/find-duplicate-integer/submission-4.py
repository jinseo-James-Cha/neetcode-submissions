class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        range 1 - n
        len5 -> range 1 - 5 inclusive

        Follow up
        1. without modifying nums -> not sorting..
        2. on O(1) extra space
        """
        # Binary Search -> TC: O(n log n ) + SC: O(1)
        n = len(nums)
        low = 1
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)

            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid
        return low

        
        # Hashset -> TC:O(n) + SC: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1


        # sorting -> O(n log n)
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if prev == num:
                return num
            prev = num
        return -1

        # brute force -> O(n^2)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1