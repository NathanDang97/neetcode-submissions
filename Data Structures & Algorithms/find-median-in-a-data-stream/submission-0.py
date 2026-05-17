class MedianFinder:

    def __init__(self):
        # min_heap to keep track of the upper half
        # max_heap to keep track of the lower half
        self.min_heap, self.max_heap = [], []
        
    def addNum(self, num: int) -> None:
        # add number to the apppropriate half
        if self.max_heap and num < self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        # rebalance the heaps if needed
        # the idea is to keep the difference in lengths of both heaps to at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, val)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2.0
        
        