class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        newStart, newEnd = newInterval

        # every ith inverval is either: (1) completely after the new interval,
        # (2) completely before the new interval, or (3) overlap with the new interval
        for i in range(len(intervals)):
            currStart, currEnd = intervals[i]
            # case (1), insert the new interval at this position and attach the remaining intervals afterwards
            if newEnd < currStart:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:] # no more merge after this point
            # case (2), leave the current interval as it is
            if newStart > currEnd:
                new_intervals.append(intervals[i])
            # case (3), merge the new interval with the current one for the next iteration
            else:
                newStart = min(newStart, currStart)
                newEnd = max(newEnd, currEnd)
                newInterval = [newStart, newEnd]
        
        # if the loop ends, it means the new interval belongs at the end of the list
        new_intervals.append(newInterval)
        return new_intervals