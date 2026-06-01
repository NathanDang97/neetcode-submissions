class Solution:
    # min-heap solution, time O(n + klog n), space O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            min_heap.append((distance, x, y))
        heapq.heapify(min_heap)

        closest_points = []
        while k > 0:
            _, x, y = heapq.heappop(min_heap)
            closest_points.append([x, y])
            k -= 1

        return closest_points