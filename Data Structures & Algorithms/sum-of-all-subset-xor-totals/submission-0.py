class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        xor

        3 = 1 1
        1 = 0 1

        """
        # Backtracking
        def backtrack(idx, subset):
            nonlocal res

            xor = 0
            for num in subset:
                xor ^= num
            res += xor

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        res = 0
        backtrack(0, [])
        return res