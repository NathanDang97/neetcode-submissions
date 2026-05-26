class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums.copy()
        heapq.heapify_max(max_heap)

        # pop the largest up to (k+1)-th largest element
        while k > 1:
            heapq.heappop_max(max_heap)
            k -= 1

        return max_heap[0]