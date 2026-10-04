from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [2 -1 1 2] k = 2

        2: [2]
        -1: [1] [-1]
        1: [2] [0] [1]
        """
        # hashmap
        res = curr = 0
        prefixSums = {0 : 1}

        for num in nums:
            curr += num
            diff = curr - k

            res += prefixSums.get(diff, 0)
            prefixSums[curr] = 1 + prefixSums.get(curr, 0)
        return res


        # Brute force -> O(n^2) -> TLE
        res = 0
        subarray = []
        for num in nums:
            if num == k:
                res += 1
            
            for i in range(len(subarray)):
                subarray[i] += num
                if subarray[i] == k:
                    res += 1
            
            subarray.append(num)
        
        return res
            