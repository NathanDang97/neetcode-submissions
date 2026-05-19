class Solution:
    # dfs solution, time and space O(V + E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        visited = set() # set of visited nodes
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # each dfs traversal only marks the neighboring nodes and not the starting node
        # so the number of components is given by the number of possible starting nodes
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                visited.add(node)
                dfs(node)

        return components