func countCharacters(words []string, chars string) int {
    charCount := make(map[rune]int)
    for _, c := range chars {
        charCount[c]++
    }

    totalLength := 0
    for _, word := range words {
        wordCount := make(map[rune]int)
        for _, c := range word {
            wordCount[c]++
        }

        valid := true
        for c, count := range wordCount {
            if count > charCount[c] {
                valid = false
                break
            }
        }

        if valid {
            totalLength += len(word)
        }
    }

    return totalLength
}