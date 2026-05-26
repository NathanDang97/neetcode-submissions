class Solution:
    # solution using min-heap, O(k) space, O((n - k)logk) time
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]