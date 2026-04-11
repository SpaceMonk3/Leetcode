"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sorting intervals in ascending order by comparing end1 & start2
        # using a lambda function in sort() and the 'key' argument
        intervals.sort(key = lambda x: x.start)

        # checking for overlaps
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True