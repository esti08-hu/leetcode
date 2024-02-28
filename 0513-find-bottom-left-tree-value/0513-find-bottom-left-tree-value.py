class Solution:
    def findBottomLeftValue(self, root):
        queue = deque([root])

        while queue:
            current = queue.popleft()

            if current.right:
                queue.append(current.right)

            if current.left:
                queue.append(current.left)

        return current.val
