"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        half open interval
        """
        if not intervals:
            return True
            
        intervals.sort(key=lambda x: x.start)

        prevEnd = intervals[0].end
        for i in intervals[1:]:
            if i.start < prevEnd:
                return False
            else:
                prevEnd = max(prevEnd, i.end)
        return True