class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers in ascending order
        return a pair index, sum equals to target and index + 1 

        num1 + num2 == target
        num2 == target - num1
        """

        # hashmap
        hashmap = {}
        for i, num in enumerate(numbers):
            if num in hashmap:
                return [hashmap[num] + 1, i + 1]
            
            hashmap[target - num] = i
        return [-1, -1]


        # brute force -> o(n^2) -> TLE
        for i in range(len(numbers) - 1):
            curr_num = numbers[i]
            for j in range(i + 1, len(numbers)):
                if curr_num + numbers[j] == target:
                    return [i+1, j+1]
        
        return [-1,-1]
























        # two pointers
        left = 0 
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]