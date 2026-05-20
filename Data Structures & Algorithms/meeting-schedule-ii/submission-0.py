"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # min-heap solution
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            # reuse the room (i.e. pop the heap) if it is not empty
            # and the earliest end time is less that or equal to the start of the next meeting
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)