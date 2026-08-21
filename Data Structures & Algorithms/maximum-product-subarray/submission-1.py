class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]        
        curr_min = 1
        curr_max = 1
        for num in nums:
            temp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(temp, num * curr_min, num)
            res = max(res, curr_max)
        return res


        # brute force
        # O(n^2) -> TLE
        max_product = max(nums)
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            max_product = max(max_product, curr)
            for j in range(i+1, n):
                curr *= nums[j]
                max_product = max(max_product, curr)
        
        return max_product

