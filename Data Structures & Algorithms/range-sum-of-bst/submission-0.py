# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS solution, O(n) time, O(h) space
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr_sum = 0

        def dfs(node, low, high):
            nonlocal curr_sum
            if not node:
                return 0
            
            if low <= node.val <= high:
                curr_sum += node.val

            dfs(node.left, low, high)
            dfs(node.right, low, high)

        dfs(root, low, high)
        return curr_sum