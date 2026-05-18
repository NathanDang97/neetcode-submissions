class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the intervals by starting points
        intervals.sort(key=lambda x: x[0])
        curr_endpoint = intervals[0][1]
        removes = 0

        for next_interval in intervals[1:]:
            # if the invervals overlap, increment the number of removes
            # and set curr_endpoint to the min of the two endpoints
            if curr_endpoint > next_interval[0]:
                removes += 1
                curr_endpoint = min(curr_endpoint, next_interval[1])
            # if not, update curr_endpoint to the current interval's endpoint
            else:
                curr_endpoint = next_interval[1]

        return removes
