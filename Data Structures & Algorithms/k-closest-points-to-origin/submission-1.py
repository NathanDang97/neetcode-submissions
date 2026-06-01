class Solution:
    # max-heap solution, time O(nlog k), space O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush_max(max_heap, (distance, x, y))
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

        closest_points = []
        while max_heap:
            _, x, y = heapq.heappop_max(max_heap)
            closest_points.append([x, y])

        return closest_points