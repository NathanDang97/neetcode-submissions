class TimeMap:
    # hash map and binary search solution
    # O(1) for set() and O(log n) time for get(), O(m * n) space
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        status, tuples = "", self.time_map[key]

        # since the values were added to the map in increasing timestamp
        # we can use binary search to find the desired value
        l, r = 0, len(tuples) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if tuples[mid][1] <= timestamp:
                status = tuples[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return status
