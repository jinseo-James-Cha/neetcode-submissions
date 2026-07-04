class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        i + j + k == 0
        => i + j = -k
        """
        def find_two_sums(arr, target):
            found = []
            left = 0
            right = len(arr) - 1
            while left < right:
                curr = arr[left] + arr[right]
                if curr == target:
                    found.append([-target, arr[left], arr[right]])
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
            triplets = find_two_sums(nums[i+1:], -nums[i])
            for triple in triplets:
                t = tuple(triple)
                if t not in found_triplets:
                    found_triplets.add(t)
                    res.append(triple[:])
        return res