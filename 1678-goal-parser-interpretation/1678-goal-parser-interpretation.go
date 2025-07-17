func interpret(command string) string {
	result := ""
	for i := 0; i < len(command); i++ {
		if command[i] == 'G' {
			result += "G"
		} else if command[i] == '(' {
			if command[i+1] == ')' {
				result += "o"
				i++
			} else if command[i+1] == 'a' {
				result += "al"
				i += 3
			}
		}
	}
	return result
}