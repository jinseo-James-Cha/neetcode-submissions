class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        i + j + k == 0
        => i + j = -k
        """
        # two pointers

        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                treeSum = nums[i] + nums[left] + nums[right]
                if treeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif treeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res


        # brute force -> o(n^3)
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i+1, n - 1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        
        return list(res)
