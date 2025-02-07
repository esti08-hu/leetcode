class Solution:
    def rotate_90(self, mat: List[List[int]]) -> List[List[int]]:
        col = len(mat)
        row = len(mat[0])
        rotated = []

        for c in range(row):
            new_row = [mat[r][c] for r in range(col)]
            rotated.append(new_row[::-1])
        
        return rotated

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat==target:
                return True
            mat = self.rotate_90(mat)
        
        return False


        