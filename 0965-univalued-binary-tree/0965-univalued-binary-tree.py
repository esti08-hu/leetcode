# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        # print(root)
        def bfs(node):
            if not node:
                return True
            if node.val != value:
                # print(node.val)
                return False
                
            dq = deque([node])

            while dq:
                node = dq.popleft()

                if not bfs(node.left) or not bfs(node.right):
                    return False

            return True
            
        return bfs(root)