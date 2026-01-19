class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols
        mat = []

        max_c = cStart + 1
        max_r = rStart + 1
        min_c = cStart - 1
        min_r = rStart - 1 
        mat.append([rStart, cStart])
        r, c = rStart, cStart
        while len(mat) < rows*cols:
            # right
            while c+1 <= max_c:
                c += 1
                if inBound(r, c):
                    mat.append([r, c])
            max_c += 1
            # down
            while r+1 <= max_r:
                r += 1
                if inBound(r, c):
                    mat.append([r, c])
            max_r += 1
            # left
            while c-1 >= min_c:
                c -= 1
                if inBound(r, c):
                    mat.append([r, c])
            min_c -= 1
            # up
            while r-1 >= min_r:
                r -= 1
                if inBound(r, c):
                    mat.append([r, c])
            min_r -= 1
        
        return mat