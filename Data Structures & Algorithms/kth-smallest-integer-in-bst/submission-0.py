# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Inorder Traversal solution, O(n) time and space
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # for a BST, Inorder Traversal always gives values in sorted order
        # so we simply store the inorder traversal in an array and return the (k-1)-th element (0-indexed)
        vals = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            vals.append(node.val)
            in_order(node.right)
        
        in_order(root)
        return vals[k - 1]