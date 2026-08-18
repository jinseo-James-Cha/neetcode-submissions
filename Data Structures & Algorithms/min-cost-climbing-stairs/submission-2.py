class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        cost[i] = cost of taking a step from ith floor
        after the i, you can go either i+1 or i+2

        starting point either 0 or 1

        top floor = n + 1
        n = len(cost)

        0 1 2 3 ... n
        n에 도착하려면
        n-1까지의 최솟값 + cost[n-1]
        n-2까지의 최솟값 + cost[n-2]
        """
        # DP - bottom up space opmitized
        n = len(cost)
        if n <= 1:
            return 0
        
        one_back = 0
        two_back = 0
        for i in range(2, n+1):
            curr = min(one_back + cost[i-1], two_back + cost[i-2])
            two_back = one_back
            one_back = curr
        return one_back


        # DP - bottom up
        n = len(cost)
        if n <= 1:
            return 0
        
        dp = [0] * (n+1)
        for i in range(2, n+1):
            one_back = dp[i-1] + cost[i-1]
            two_back = dp[i-2] + cost[i-2]
            dp[i] = min(one_back, two_back)
        return dp[n]


        # DP - top down
        def dp(idx):
            if idx <= 1:
                return 0
            
            if idx not in memo:
                one_back = dp(idx-1) + cost[idx - 1]
                two_back = dp(idx-2) + cost[idx - 2]
                memo[idx] = min(one_back, two_back)
            
            return memo[idx]


        memo = {}
        return dp(len(cost))