# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iteration solution, O(h) time, O(1) space
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr = root
        while curr:
            if val > curr.val:
                # insert if there is no right node
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                # otherwise, move on
                curr = curr.right
            else:
                # insert if there's no left node
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                # otherwise, move on
                curr = curr.left