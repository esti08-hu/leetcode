func restoreString(s string, indices []int) string {
	result := make([]byte, len(s))
	for i, char := range s {
		result[indices[i]] = byte(char)
	}
	return string(result)
}