from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        queue = deque([root])
        level = 0

        while queue:
            prev_val = None
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if level % 2 == 0:  # Even level
                    if node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:  # Odd level
                    if node.val % 2 != 0 or (prev_val is not None and node.val >= prev_val):
                        return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True