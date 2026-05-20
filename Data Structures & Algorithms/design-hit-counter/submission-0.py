class HitCounter:
    # solution using a queue, O(1) time for hit, O(n) time for getHits
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            diff = timestamp - self.hits[0]
            if diff >= 300:
                self.hits.popleft()
            else:
                break

        return len(self.hits)