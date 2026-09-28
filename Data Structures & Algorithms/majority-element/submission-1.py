class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res


        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res