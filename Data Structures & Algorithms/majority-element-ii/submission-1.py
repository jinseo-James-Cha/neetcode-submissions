class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # boys moore? election algorithm
        # top 2 majorities
        # first = second = float('-inf')
        # first_count = second_count = 0
        # for num in nums:
        #     if first == num:
        #         first_count += 1
        #     elif second == num:
        #         second_count += 1
            

        count = Counter(nums)
        res = []

        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)

        return res

        
        # brute force -> o(n^2) -> TLE
        res = set()
        n = len(nums)
        for i in range(n):
            curr_count = 1
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    curr_count += 1
            
            if curr_count > n / 3:
                res.add(nums[i])
        
        return list(res)