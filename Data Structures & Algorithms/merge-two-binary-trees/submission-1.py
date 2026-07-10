# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS solution, O(n + m) time, O(n + m) space
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque()
        queue.append((root1, root2))

        while queue:
            curr_node1, curr_node2 = queue.popleft()
            curr_node1.val += curr_node2.val
            
            # handle the left subtree
            if curr_node1.left and curr_node2.left:
                queue.append((curr_node1.left, curr_node2.left))
            elif not curr_node1.left:
                curr_node1.left = curr_node2.left

            # handle the right subtree
            if curr_node1.right and curr_node2.right:
                queue.append((curr_node1.right, curr_node2.right))
            elif not curr_node1.right:
                curr_node1.right = curr_node2.right
        
        return root1