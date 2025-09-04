func sortString(s string) string {
	r := []rune(s)
	for i := 0; i < len(r); i++ {
		for j := i + 1; j < len(r); j++ {
			if r[j] < r[i] {
				r[i], r[j] = r[j], r[i]
			}
		}
	}
	return string(r)
}

func groupAnagrams(strs []string) [][]string {
	anagramMap := make(map[string][]string)
	
	for _, str := range strs {
		sortedStr := sortString(str)
		anagramMap[sortedStr] = append(anagramMap[sortedStr], str)
	}
	
	var result [][]string
	for _, group := range anagramMap {
		result = append(result, group)
	}
	
	return result
}