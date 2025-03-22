# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

            def bfs(root):
                dq = deque([root])
                lvl = 0
                while dq:
                    l = len(dq)
                    if lvl%2:
                        l,r = 0,l-1
                        while l<r:
                            dq[l].val, dq[r].val = dq[r].val, dq[l].val
                            l+=1
                            r-=1

                    for _ in range(len(dq)):
                        node = dq.popleft()
                        if node.left:
                            dq.append(node.left)
                        if node.right:
                            dq.append(node.right)
                    lvl+=1
                
            bfs(root)
            return root

                        
        
            
