from collections import defaultdict
class Solution:
    # Kahn's Algorithm solution, O(V + E) time and space
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # construct the undirected graph and compute the in-degrees of the nodes
        n = len(edges)
        graph = defaultdict(list)
        in_degrees = [0] * (n + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degrees[u] += 1
            in_degrees[v] += 1

        # run Kahn's algorithm to "trim" the in degrees of the nodes in topological order
        # initialize the queue with nodes having in degrees of 1 (these can't form a cycle)
        queue = deque()
        for node in range(1, n + 1):
            if in_degrees[node] == 1:
                queue.append(node)

        while queue:
            curr_node = queue.popleft()
            in_degrees[curr_node] -= 1
            for neighbor in graph[curr_node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 1:
                    queue.append(neighbor)

        # at this points, nodes with in degrees > 0 can form cycles
        # we traverse the input edges in reversed order to return the edge that appears last in the input
        for u, v in reversed(edges):
            if in_degrees[u] > 1 and in_degrees[v] > 0:
                return [u, v]
        
        return []
        