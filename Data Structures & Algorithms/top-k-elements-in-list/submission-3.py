class Solution:
    # min-heap solution, O(nlogk) time, O(n + k) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency counter of each element
        counter = Counter(nums)
        
        # use min_heap to keep track of the top k most frequent elements
        # this works because as the size of the heap > k, we pop the current least frequent element
        min_heap = []
        for num, frequency in counter.items():
            heapq.heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        top_k_frequent = []
        for i in range(k):
            top_k_frequent.append(heapq.heappop(min_heap)[1])
        return top_k_frequent

        