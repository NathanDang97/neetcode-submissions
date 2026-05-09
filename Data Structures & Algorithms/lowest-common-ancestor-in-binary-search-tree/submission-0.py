# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # general solution that works for all binary trees, O(h) time and space, h: height of tree
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, p, q):
            if not node or node.val == p.val or node.val == q.val:
                return node

            left_lca = dfs(node.left, p, q)
            right_lca = dfs(node.right, p, q)

            if left_lca and right_lca:
                return node

            return left_lca if left_lca else right_lca

        return dfs(root, p, q)