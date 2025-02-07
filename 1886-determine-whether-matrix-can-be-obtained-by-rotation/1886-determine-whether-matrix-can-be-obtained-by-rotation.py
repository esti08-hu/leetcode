class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        col = len(mat)
        row = len(mat[0])

        rotate_mat = []
        for c in range(row):
            new_row = []

            for r in range(col):
                new_row.append(mat[r][c])
            print(new_row[::-1])
            rotate_mat.append(new_row[::-1])

        if rotate_mat == target:
            return True
        else:
            mat = rotate_mat
            rotate_mat = []
            for c in range(row):
                new_row = []

                for r in range(col):
                    new_row.append(mat[r][c])
                print(new_row[::-1])
                rotate_mat.append(new_row[::-1])

            print(rotate_mat, target)

            if rotate_mat == target:
                return True
            else:
                mat = rotate_mat
                rotate_mat = []
                for c in range(row):
                    new_row = []

                    for r in range(col):
                        new_row.append(mat[r][c])
                    print(new_row[::-1])
                    rotate_mat.append(new_row[::-1])

                print(rotate_mat, target)

                if rotate_mat == target:
                    return True
        
        return False



