class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        half-open interval
        [[1,2],[2,4],[1,4]]

        1 2 3 4 
        - -
          - - -
        - - - -

        [[0,2],[1,3],[2,4],[3,5],[4,6]]
        
        0 1 2 3 4 5 6
        - - -
          - - -
            - - -
              - - -
                - - -
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res