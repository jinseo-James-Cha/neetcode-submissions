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
        """

        # binary search for k and check total hours
        piles.sort()
        left = 1 # minimum k
        right = piles[-1] # maximum k

        min_rate = right
        while left <= right:
            mid_rate = (left + right) // 2
            curr_total_hour = 0
            for p in piles:
                curr_total_hour += p // mid_rate
                curr_total_hour += 1 if p % mid_rate > 0 else 0
            
            if curr_total_hour <= h:
                min_rate = min(min_rate, mid_rate)
                right = mid_rate - 1
            else:
                left = mid_rate + 1
        return min_rate





