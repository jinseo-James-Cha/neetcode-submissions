class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashset
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
        # bucket
        # time: O(n + k), k = max_num - min_num
        # space: O(k)

        if not nums:
            return 0

        max_num = max(nums)
        min_num = min(nums)
        buckets = [False] * (max_num - min_num + 2)

        for num in nums:
            buckets[num - min_num] = True
        
        longest = 1
        current = 0
        for i in range(len(buckets)):
            if buckets[i]:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
        return longest