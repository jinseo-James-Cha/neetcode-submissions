class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas station with circular

        gas     1 2 3 4
        cost    2 2 4 1
                      1 start with tank 4
                2 tank 4 and - cost[3] + gas[0] = 4

                1 2 3 4
                2 2 4 1
                -------
                -1 0 -1 3
                
                5 8 2 8
                6 5 6 6
                -------
                -1 3 -4 2
                -1 2 -2 0

        """
        # Greedy
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
        return res
        





        # Brute force -> TLE
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            new_gas = gas[i:] + gas[:i]
            new_cost = cost[i:] + cost[:i]
            curr_tank = 0
            flag = True
            for ng, nc in zip(new_gas, new_cost):
                curr_tank += ng
                if curr_tank < nc:
                    flag = False
                    break
                curr_tank -= nc
            
            if flag:
                return i
        return -1






        