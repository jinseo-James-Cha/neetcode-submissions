class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        x + y = target
        x = target - y
        x == current value
        target - y == target - prev value
        """
        saved_idx = {}
        for i, num in enumerate(nums):
            if num in saved_idx:
                return [saved_idx[num], i]
            
            saved_idx[target-num] = i
        return [-1,-1]