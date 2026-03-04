class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        tree = [[] for _ in range(n)]
        not_root = set()
        found_0 = False
        for i in range(n):
            if leftChild[i]!=-1:
                tree[i].append(leftChild[i])
                not_root.add(leftChild[i])
            if rightChild[i]!=-1:
                tree[i].append(rightChild[i])
                not_root.add(rightChild[i])

        if len(not_root) != n-1:
            return False
        root = None
        for i in range(n):
            if i not in not_root:
                root = i
                break

        self.seen = set()

        def dfs(node):
            if node in self.seen:
                return False
            self.seen.add(node)
            for child in tree[node]:
                if not dfs(child):
                    return False
            return True

        return dfs(root) and len(self.seen) == n
        