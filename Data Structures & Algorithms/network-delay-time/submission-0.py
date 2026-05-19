class Solution:
    # dfs solution, time O(V * E), space O(V + E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        distance = {node: float('inf') for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= distance[node]:
                return

            distance[node] = time
            for neighbor, t in graph[node]:
                dfs(neighbor, t + time)

        dfs(k, 0)
        result = max(distance.values())
        return result if result < float('inf') else - 1