# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative DFS solution, O(n) time and space
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        curr_sum = 0

        while stack:
            curr_node = stack.pop()
            if not curr_node:
                continue
            
            if low <= curr_node.val <= high:
                curr_sum += curr_node.val
            
            if curr_node.val > low:
                stack.append(curr_node.left)
            if curr_node.val < high:
                stack.append(curr_node.right)

        return curr_sum
        