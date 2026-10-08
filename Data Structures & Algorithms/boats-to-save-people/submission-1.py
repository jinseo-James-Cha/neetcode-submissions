class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        people[i] = weight[i]

        infinite number of boats
        a boat carries at most two people

        return minimum number of boats

        1 3 2 3 2

        1 2 2 3 3
        L       R
              R B
        L R   B B
        B LR B
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
