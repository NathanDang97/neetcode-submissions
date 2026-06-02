"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # BFS solution, O(V + E) time and space
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        deep_copy = defaultdict(Node)
        deep_copy[node] = Node(node.val)
        queue = deque()
        queue.append(node)

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in deep_copy:
                    deep_copy[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                deep_copy[curr_node].neighbors.append(deep_copy[neighbor])

        return deep_copy[node]
