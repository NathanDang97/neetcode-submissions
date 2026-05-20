class HitCounter:
    # a more optimized solution using a queue
    # there might be a case where many hits occured in a single timestamp
    # so we store a tuple (timestamp, its frequency) to the queue instead of just the timestamp
    # O(1) time for hit, O(n) time for getHits (but more or less O(1) in average)
    def __init__(self):
        self.hits = deque()
        # note that using the new strategy, this is no longer simply the size of the queue
        self.count = 0 # the number of hits needed to return

    def hit(self, timestamp: int) -> None:
        self.count += 1
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.hits[0][1] -= 1
            if self.hits[0][1] == 0:
                self.hits.popleft()
            self.count -= 1

        return self.count