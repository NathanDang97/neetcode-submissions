from collections import defaultdict
import heapq

class Solution:
    # Prim's algorithm solution to construct MST
    # O(n^2 logn) time, O(n^2) space
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        graph = defaultdict(list)
        for i in range(num_points):
            x1, y1 = points[i]
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((distance, j))
                graph[j].append((distance, i))

        min_heap = [(0, 0)]
        min_cost = 0
        visited = set()

        while len(visited) < num_points:
            curr_distance, curr_point = heapq.heappop(min_heap)
            if curr_point in visited:
                continue
            visited.add(curr_point)
            min_cost += curr_distance

            for next_distance, next_point in graph[curr_point]:
                if next_point not in visited:
                    heapq.heappush(min_heap, (next_distance, next_point))

        return min_cost

