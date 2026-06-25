from collections import defaultdict
class Solution:
    # sweep-line solution, O(nlogn) time, O(n) space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sweep_line = defaultdict(int)
        for interval in intervals:
            sweep_line[interval[0]] += 1
            sweep_line[interval[1]] -= 1

        merged = []
        curr_interval = []
        active_intervals = 0 # track the number of current active intervals

        for i in sorted(sweep_line):
            # begin a new interval
            if not curr_interval:
                curr_interval.append(i)

            # when active_intervals goes from 0 to positive, a merge begins
            # when active_intervals goes from positive to 0, a merge ends
            active_intervals += sweep_line[i]
            if active_intervals == 0:
                curr_interval.append(i)
                merged.append(curr_interval)
                curr_interval = [] # reset to begin a new interval

        return merged
            