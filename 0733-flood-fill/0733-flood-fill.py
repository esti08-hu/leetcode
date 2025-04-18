class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        q = deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))
        original_color = image[sr][sc]
        image[sr][sc] = color
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row < 0 or row == rows or
                    col < 0 or col == cols or
                    image[row][col] != original_color or
                    (row, col) in visited):
                    continue

                image[row][col] = color
                q.append((row, col))
                visited.add((row, col))
        
        return image