from collections import defaultdict
import heapq
class Solution:
    # Dijsktra's Algorithm solution, O(ElogV) time, O(V + E) space
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            total_time = curr_time

            for neighbor, time in graph[curr_node]:
                if neighbor not in visited:
                    next_time = curr_time + time
                    heapq.heappush(min_heap, (next_time, neighbor))

        return total_time if len(visited) == n else -1
