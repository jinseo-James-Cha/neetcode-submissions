class Solution:
    def mySqrt(self, x: int) -> int:
        """
        0: 0
        1: 1
        2: 1
        3: 1
        
        4: 2
        5: 2
        6: 2
        7: 2
        8: 2

        9: 3
        ..
        15: 3

        16: 4

        15
        0 ~ 15
         7 * 7 > 15
        0 ~ 6
          3 * 3 < 15 res = 3
        4 ~ 6
          5 * 5 > 15
        4 ~ 4
        
        """

        left = 0
        right = x
        res = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                res = mid
            else:
                return mid
        return res


