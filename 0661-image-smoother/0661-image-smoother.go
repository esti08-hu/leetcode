func imageSmoother(img [][]int) [][]int {
    col := len(img[0])
	row := len(img)
	ans := make([][]int, row)
	
	for i := 0; i < row; i++ {
		ans[i] = make([]int, col)
		for j := 0; j < col; j++ {
			sum := 0
			count := 0
			for x := i - 1; x <= i+1; x++ {
				for y := j - 1; y <= j+1; y++ {
					if x >= 0 && x < row && y >= 0 && y < col {
						sum += img[x][y]
						count++
					}
				}
			}
			ans[i][j] = sum / count
		}
	}

	return ans
}