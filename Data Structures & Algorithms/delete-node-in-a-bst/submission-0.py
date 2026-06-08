# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution, O(h) time and space
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # search the left and right subtree for the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if found, find the in-order successor (leftmost node in the right subtree)
        else:
            # if there's no left child then simply return the right child
            if not root.left:
                return root.right
            # similar as above
            elif not root.right:
                return root.left
            # otherwise, attach the deleted node's left subtree to this in-order successor's left,
            # delete the node, and return the right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            new_root = root.right
            del root
            return new_root

        return root

