from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        dq = deque([root])

        while dq:
            lvl = []
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                lvl.append(node.val)

                if node.left:
                    dq.append(node.left)
                
                if node.right:
                    dq.append(node.right)

            lvl = list(reversed(lvl)) if len(res) % 2 else lvl
            res.append(lvl)
        
        return res