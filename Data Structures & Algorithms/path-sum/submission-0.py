# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS solution, O(n) time and space
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curr_sum, targetSum):
            if not node:
                return False
            
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            return dfs(node.left, curr_sum, targetSum) or dfs(node.right, curr_sum, targetSum)

        return dfs(root, 0, targetSum)