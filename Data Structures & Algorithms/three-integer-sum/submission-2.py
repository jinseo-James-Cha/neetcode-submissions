class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        i + j + k == 0
        => i + j = -k
        """
        def find_two_sums(left, target):
            found = []
            right = len(nums) - 1
            while left < right:
                curr = nums[left] + nums[right]
                if curr == target:
                    found.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif curr > target:
                    right -= 1
                else:
                    left += 1
            return found


        n = len(nums)
        nums.sort()
        found_triplets = set()
        res = []
        for i in range(n-2):
            triplets = find_two_sums(i + 1, -nums[i])
            for triple in triplets:
                t = tuple(triple)
                if t not in found_triplets:
                    found_triplets.add(t)
                    res.append(triple[:])
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
