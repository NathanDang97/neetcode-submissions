from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                node_p = q1.popleft()
                node_q = q2.popleft()
                if not node_p and not node_q:
                    continue

                if not node_p or not node_q or node_p.val != node_q.val:
                    return False

                q1.append(node_p.left)
                q1.append(node_p.right)
                q2.append(node_q.left)
                q2.append(node_q.right)

        return True