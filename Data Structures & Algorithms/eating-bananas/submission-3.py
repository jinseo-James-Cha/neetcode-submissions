class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        ith bananas
        h - the number of hours you have to eat all the bananas
        k - bananas-per-hour
        
        return minimum k 

        1,4,3,2 and h = 9
        1 2 2 1 and 6hours and k = 2

        1 4 3 2 and 10hours and k = 1 10hours > 9h, so wrong answer
        so k = 2

        1 2 3 4  and h = 9

        Question
        Within h, how many banana(k) should be consume per hour
        return the minimum k
        """
        
        # binary search for k
        # O( n log m) // m means maximum of piles
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            hour = 0
            for pile in piles:
                hour += pile // mid
                hour += int(pile % mid > 0)
            if hour <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res