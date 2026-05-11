# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left_depth = 1 + dfs(node.left)
            right_depth = 1 + dfs(node.right)

            return max(left_depth, right_depth)

        return dfs(root)
            