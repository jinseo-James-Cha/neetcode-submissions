class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        range 1 - n
        len5 -> range 1 - 5 inclusive

        Follow up
        1. without modifying nums -> not sorting..
        2. on O(1) extra space
        """
        # Floyd's cycle detection
        
        # put the both in the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # send one in beginning and find second meeting point 
        # => cycle entrance => return the value
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        # Binary Search -> TC: O(n log n ) + SC: O(1)
        n = len(nums)
        low = 1
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)

            # Num itself represents how many it can be if 1
            # like 3 mid -> 1, 2, 3
            # if 4 <= mid 3 means
            # it can have maximum 3 but has one more than that.
            # so answer is on low side
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