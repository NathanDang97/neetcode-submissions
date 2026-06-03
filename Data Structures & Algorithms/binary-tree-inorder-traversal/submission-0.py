# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative solution
    # in-order: left-root-right
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order = []
        stack = []
        curr = root

        while curr or stack:
            # use the stack to go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            in_order.append(curr.val)
            curr = curr.right

        return in_order