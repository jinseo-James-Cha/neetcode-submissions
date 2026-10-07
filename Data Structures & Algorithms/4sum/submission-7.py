class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        
        a + b + c + d == target
        a,b,c,d are unique
        """
        # K sum and two pointers
        nums.sort()
        res = []
        quad = []

        def kSum(k, start, target, curr_combination):
            if k == 2:
                left = start
                right = len(nums) - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    if curr_sum > target:
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        res.append(curr_combination + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return
            
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                curr_combination.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i], curr_combination)
                curr_combination.pop()
                        
        kSum(4, 0, target, [])
        return res


        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res



