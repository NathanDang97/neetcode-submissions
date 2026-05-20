"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # two-pointer solution, time O(nlogn), space O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        ongoing_meetings, rooms = 0, 0
        s, e, = 0, 0 # pointers for start and end time respectively

        while s < len(intervals):
            # a new meeting start before the earliest one ends
            if start_times[s] < end_times[e]:
                ongoing_meetings += 1
                s += 1
            # a meeting has recently ended
            else:
                ongoing_meetings -= 1
                e += 1

            rooms = max(rooms, ongoing_meetings)

        return rooms
