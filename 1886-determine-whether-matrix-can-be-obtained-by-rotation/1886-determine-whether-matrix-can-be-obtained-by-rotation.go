func compare(mat1, mat2 [][]int) bool {
	if len(mat1) != len(mat2) || len(mat1[0]) != len(mat2[0]) {
		return false
	}
	for i := range mat1 {
		for j := range mat1[i] {
			if mat1[i][j] != mat2[i][j] {
				return false
			}
		}
	}
	return true
}

func rotate(mat [][]int) [][]int {
	n := len(mat)
	rotated := make([][]int, n)
	for i := range rotated {
		rotated[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			rotated[j][n-1-i] = mat[i][j]
		}
	}
	return rotated
}

func findRotation(mat [][]int, target [][]int) bool {
	for i := 0; i < 4; i++ {
		if compare(mat, target) {
			return true
		}
		mat = rotate(mat)
	}
	return false
}
