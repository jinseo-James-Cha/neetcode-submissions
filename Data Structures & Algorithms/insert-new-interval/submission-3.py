class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """ 

        1 2 3 4 5 6 
        - - -
              - - -
          - - - -
        """
        # open intervals - both side inclusive
        i = 0
        n = len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)
        
        res.extend(intervals[i:])
        return res


