# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        Q = deque([(root.left, root.right)])
        while Q:
            left, right = Q.popleft()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            Q.append((left.left, right.right))
            Q.append((left.right, right.left))

        return True
