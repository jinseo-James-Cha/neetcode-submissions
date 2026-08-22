from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP - binary search
        stack = []
        for num in nums:
            insert_idx = bisect_left(stack, num)
            if insert_idx == len(stack):
                stack.append(num)
            else:
                stack[insert_idx] = num
        return len(stack)
        
        # monotonic stack -> X
        stack = []
        max_len = 0
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)
            max_len = max(max_len, len(stack))
        return max_len