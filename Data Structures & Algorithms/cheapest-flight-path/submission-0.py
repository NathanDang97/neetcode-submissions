from collections import defaultdict
import heapq
class Solution:
    # solution using Dijkstra's, time O(ElogV), space O(E + V)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_heap = [(0, src, -1)] # cost, node, num of stops
        min_stops = defaultdict(int) # maps a node to the minimum number of stops to reach it

        while min_heap:
            curr_cost, curr_node, curr_stops = heapq.heappop(min_heap)
            if curr_stops > k:
                continue
            # since edge costs are non-negative, more stops means either the same or more expensive
            if curr_node in min_stops and min_stops[curr_node] <= curr_stops:
                continue
            if curr_node == dst:
                return curr_cost
            min_stops[curr_node] = curr_stops

            for neighbor, weight in graph[curr_node]:
                next_cost = curr_cost + weight
                next_stops = curr_stops + 1
                heapq.heappush(min_heap, (next_cost, neighbor, next_stops))
        
        return -1