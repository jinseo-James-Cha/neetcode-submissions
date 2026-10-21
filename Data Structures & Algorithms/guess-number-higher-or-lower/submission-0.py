# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        1 ~ n and I guess which number it is

        guess(num) => tell me higher or lower
        0 -> num == pick
        -1 -> num > pick
        1 -> num < pick
        """
        left = 1
        right = n

        while left <= right:
            mid = left + ((right - left) // 2)
            
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        return left