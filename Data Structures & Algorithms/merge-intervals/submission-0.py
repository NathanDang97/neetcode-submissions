class Solution:
    # O(nlogn) solution
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        # sort the interval by left bounds
        intervals.sort(key=lambda x: x[0])
        curr_interval = intervals[0]

        for next_interval in intervals[1:]:
            # merge the right bounds if two intervals overlap
            if curr_interval[1] >= next_interval[0]:
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            # otherwise add the current interval to the merged list
            else:
                merged.append(curr_interval)
                curr_interval = next_interval

        # don't forget the last one
        merged.append(curr_interval)
        return merged