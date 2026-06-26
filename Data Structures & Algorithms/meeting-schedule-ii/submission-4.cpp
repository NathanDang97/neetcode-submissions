/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    // min-heap solution, O(nlogn) time, O(n) space
    int minMeetingRooms(vector<Interval>& intervals) {
        // sort the intervals by start time
        auto comparator = [](auto& a, auto& b) {return a.start < b.start;};
        sort(intervals.begin(), intervals.end(), comparator);
        // the min heap stores the end time of the intervals
        priority_queue<int, vector<int>, greater<int>> minHeap;

        // reuse the room (i.e. pop the heap) if it is not empty
        // when the earliest end time is less than or equal to the start of the next meeting
        for (const auto& interval : intervals) {
            if (!minHeap.empty() && minHeap.top() <= interval.start) {
                minHeap.pop();
            }
            minHeap.push(interval.end);
        }
        return minHeap.size();
    }
};
