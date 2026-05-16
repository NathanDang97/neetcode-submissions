class Solution:
    # max-heap solution, O(nlogk) time
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency count of each element
        counter = Counter(nums)

        # construct the max heap
        max_heap = [(value, key) for key, value in counter.items()]
        heapq.heapify_max(max_heap)

        # get the top k most frequent elements
        result = []
        while k > 0:
            _, value = heapq.heappop_max(max_heap)
            result.append(value)
            k -= 1

        return result
