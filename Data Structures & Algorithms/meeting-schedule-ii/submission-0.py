"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        half open intervals
        """
        if not intervals:
            return 0
        
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort()

        curr_room = 0
        max_room = 0
        for time, score in events:
            curr_room += score
            max_room = max(max_room, curr_room)
        return max_room
        



