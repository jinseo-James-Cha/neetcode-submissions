class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        people[i] = weight[i]

        infinite number of boats
        a boat carries at most two people

        return minimum number of boats

        max(people) <= limit, so maximum is always needed to add
        and then check if lightest one can fit in the boat
        so, 
        heaviest + lightest
        """
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats
