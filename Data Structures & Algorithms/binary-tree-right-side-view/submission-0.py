# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # idea: use BFS
        right_side_view = []
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # update the right most value as we process the current level
                right_most_value = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            right_side_view.append(right_most_value)

        return right_side_view