class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        min_counts = Counter(words[0])
        for word in words[1:]:
            word_count = Counter(word)
            for char in min_counts:
                min_counts[char] = min(min_counts[char], word_count.get(char, 0))

        return [char for char, count in min_counts.items() for _ in range(count)]