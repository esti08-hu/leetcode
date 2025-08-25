func findRestaurant(list1 []string, list2 []string) []string {
	restMap := make(map[string]int)
	for i, rs := range list1 {
		restMap[rs] = i
	}

	minIndexSum := math.MaxInt32
	var res []string
	for i, rs := range list2 {
		if index, found := restMap[rs]; found {
			indexSum := i + index
			if indexSum < minIndexSum {
				minIndexSum = indexSum
				res = []string{rs}
			} else if indexSum == minIndexSum {
				res = append(res, rs)
			}
		}
	}
	return res
}