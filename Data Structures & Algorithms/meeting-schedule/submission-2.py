"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # sorting solution, O(nlogn) time, O(1) space (or O(n) space depending on the sorting algorithm)
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x.start)
        curr_meeting = intervals[0]

        for next_meeting in intervals[1:]:
            # check the end time of the current meeting vs the start time of the next one
            curr_end = curr_meeting.end
            next_start = next_meeting.start
            if curr_end > next_start:
                return False
            
            # update the current meeting
            curr_meeting = next_meeting

        return True