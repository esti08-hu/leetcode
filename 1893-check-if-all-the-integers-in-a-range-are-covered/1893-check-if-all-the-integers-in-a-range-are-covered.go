func isCovered(ranges [][]int, left int, right int) bool {
	for i := left; i <= right; i++ {
		covered := false
		for _, r := range ranges {
			if r[0] <= i && i <= r[1] {
				covered = true
				break
			}
		}
		if !covered {
			return false
		}
	}
	return true
}