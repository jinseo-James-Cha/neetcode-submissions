class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        positive integers and target
        return the minimal length of subarray
        sum(res) >= target

        2 1 5 1 5 3
            L
                R

        2 3 8 9 14
        """

        curr_sum = 0
        min_len = float('inf')
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                
                curr_sum -= nums[left]
                left += 1
            
                
        return min_len if min_len != float('inf') else 0