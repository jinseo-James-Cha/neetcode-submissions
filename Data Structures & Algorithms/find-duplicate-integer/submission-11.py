class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
        
        
        # binary search
        n = len(nums)
        left = 1
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)
            if lessOrEqual <= mid:
                left = mid + 1
            else:
                right = mid
        return left
        
        # without modifying array
        # O(n) + O(n)
        check = [False] * (len(nums) + 1)
        for num in nums:
            if check[num]:
                return num
            check[num] = True
        return -1

        # sort
        # O(n log n) + O(1)
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return nums[i]
        return -1

        # brute force - hashset
        # O(n) and O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1