class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        send all weights within days
        what is minimum weights?

        2 4 6 1 3 10 within 4 days
        2
          4 6
              1 3 
                  10
        """
        if len(weights) <= days:
            return max(weights)
        
        left = max(weights)
        right = sum(weights)
        res = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            day = 1
            curr = mid
            for weight in weights:
                if curr - weight >= 0:
                    curr -= weight
                else:
                    day += 1
                    curr = mid - weight
            
            if day <= days:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res

