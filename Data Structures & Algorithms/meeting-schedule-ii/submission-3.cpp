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
    // sweep-line algorithm, O(nlogn) time, O(n) space
    int minMeetingRooms(vector<Interval>& intervals) {
        map<int, int> sweepLine; // use ordered map to auto-sort the pairs by keys
        for (const auto& interval : intervals) {
            sweepLine[interval.start]++;
            sweepLine[interval.end]--;
        }

        int ongoingMeetings = 0;
        int rooms = 0;
        for (const auto& [key, value] : sweepLine) {
            ongoingMeetings += value;
            rooms = max(rooms, ongoingMeetings);
        }

        return rooms;
    }
};
