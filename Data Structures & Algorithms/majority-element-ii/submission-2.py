from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # boyer-moore? election algorithm
        # top 2 majorities
        n = len(nums)
        first = second = -1
        first_count = second_count = 0
        cnt = defaultdict(int)

        for num in nums:
            if first == num:
                first_count += 1
            elif second == num:
                second_count += 1
            elif first_count == 0:
                first = num
                first_count += 1
            elif second_count == 0:
                second = num
                second_count += 1
            else:
                first_count -= 1
                second_count -= 1
            
            cnt[num] += 1
        
        res = []
        if cnt[first] > n // 3:
            res.append(first)
        if cnt[second] > n // 3:
            res.append(second)
        return res

            
        
            

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