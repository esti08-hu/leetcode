class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []

        a_set = set()
        p_set = set()
        def toPac(r, c, visited):
            if (r == 0 or c == 0 or 
                (r, c) in p_set):
                return 1

            if (r < 0 or r == rows or 
                c < 0 or c == cols or 
                (r, c) in visited):
                return 0

            visited.add((r, c))

            res = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr in range(rows) and nc in range(cols) and heights[r][c] >= heights[nr][nc]):
                    res += toPac(nr, nc, visited)
                    if res:
                        return res
            return res

        def toAtl(r, c, visited):
            if (r == rows-1 or c == cols-1 or 
                (r, c) in a_set):
                return 1

            if (r < 0 or r == rows or 
                c < 0  or c == cols or 
                (r, c) in visited):
                return 0

            visited.add((r, c))

            res = 0
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr in range(rows) and nc in range(cols) and heights[r][c] >= heights[nr][nc]):
                        res += toAtl(nr, nc, visited)
                        if res:
                            return res
            return res

        for r in range(rows):
            for c in range(cols):
                pac = toPac(r, c, set())
                atl = toAtl(r, c, set())

                if pac and atl:
                    a_set.add((r, c))
                    p_set.add((r, c))
                    res.append([r, c])
                elif pac:
                    p_set.add((r, c))
                elif atl:
                    a_set.add((r, c))

        return res
