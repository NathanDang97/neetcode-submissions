class KthLargest:
    # min-heap solution, use the heap to keep track of the k largest elements
    # the minimum of these values is the desired kth largest element
    # O(m * logk) time, O(k) space
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
