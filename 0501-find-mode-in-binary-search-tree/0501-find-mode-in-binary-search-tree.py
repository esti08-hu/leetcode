# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.dct = defaultdict(int)

        def dfs(root):
            if not root:
                return

            self.dct[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        if not self.dct:
            return []
        mode = max(self.dct.values())
        res = []
        for k, v in self.dct.items():
            if v == mode:
                res.append(k)
        
        return res