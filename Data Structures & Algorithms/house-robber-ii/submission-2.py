class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        circle house -> first and last are neighbors
        cannot rob two adjacent houses

        return the maximum amount

        3 4 3 -> 3 4 3
        3 4 and think take prev or prevprev + mine?
        but mine is not available cuz of last one
        I can take mine or first one

        so, for the last house, we need to think max(last, first) + two prev

        2 9 8 3 6
        2   8   6 -> 2 and 6 are neighbors
          9     6

        think separately.
        we can choose either the first one or last one.
        excluding first one
        - 9 8 3 6
        excluding last one
        2 9 8 3 -
        and then find the bigger one
        """
        # DP - bottom up, space optimized
        if len(nums) == 1:
            return nums[0]
        
        def dp(houses):
            n = len(houses)
            if n == 1:
                return houses[0]

            two_back = houses[0]
            one_back = max(houses[0], houses[1])
            for i in range(2, n):
                curr = max(two_back + houses[i], one_back)
                two_back = one_back
                one_back = curr
            return one_back
            
        return max(dp(nums[1:]), dp(nums[:-1]))


        # DP - bottom up
        if len(nums) == 1:
            return nums[0]
        
        def dp(houses):
            n = len(houses)
            if n == 1:
                return houses[0]

            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            
            return dp[-1]
        return max(dp(nums[1:]), dp(nums[:-1]))



        # DP - top down - TLE
        if len(nums) == 1:
            return nums[0]

        def dp(n, houses ,memo):
            if n == 0:
                return houses[0]
            elif n == 1:
                return max(houses[0], houses[1])

            memo[n] = max(dp(n-2, houses, memo) + houses[n], dp(n-1, houses, memo))
            return memo[n]
        
        return max(dp(len(nums)-2, nums[1:], {}), dp(len(nums)-2, nums[:-1], {}))