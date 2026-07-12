# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS solution, O(n) time and space
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        order = []

        # BFS to visit every node and record traversal order
        while queue:
            curr_node = queue.popleft()
            order.append(curr_node)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        # process nodes in *reversed* BFS order (children before parents)
        # so that by the time we reach a node, both its children's heights
        # are already known.
        diameter = 0
        height = defaultdict(int)
        for node in reversed(order):
            left_height = height[node.left]
            right_height = height[node.right]
            diameter = max(diameter, left_height + right_height)
            height[node] = 1 + max(left_height, right_height)

        return diameter