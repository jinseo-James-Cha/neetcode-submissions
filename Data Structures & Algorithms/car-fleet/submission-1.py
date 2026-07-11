class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        n cars

        - - - - - - - - -
          C     C
        
        1 4
        3 2

        4 6
        7 8
        10 10

        4 1 0 7
        2 2 1 1

        6 3 1 8
        8 5 2 9
        10 7 3 10

        4 + 2 * x >= target
        2  * x >= target - 4 
        x >= target - 4 / 2
        
        x = 3
        """
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


