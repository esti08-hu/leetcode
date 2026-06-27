# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        hash_map = defaultdict(int)
        hash_map[root.val] = -1
        q = deque()
        q.append(root)
        found = False

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                del hash_map[node.val]

                if node.left:
                    q.append(node.left)
                    hash_map[node.left.val] = node.val
                    if (node.left.val == x or node.left.val == y) and not found:
                        found = True

                if node.right:
                    q.append(node.right)
                    hash_map[node.right.val] = node.val
                    if (node.right.val == x or node.right.val == x) and not found:
                        found = True
            
            if found:
                if hash_map[x] != 0 and hash_map[y] != 0 and hash_map[x] != hash_map[y]:
                    return True
                else:
                    return False
        
        return False