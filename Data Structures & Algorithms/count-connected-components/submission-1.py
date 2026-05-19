class Solution:
    # bfs solution, O(V + E) time and space
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                curr_node = queue.popleft()
                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                visited.add(node)
                bfs(node)

        return components
