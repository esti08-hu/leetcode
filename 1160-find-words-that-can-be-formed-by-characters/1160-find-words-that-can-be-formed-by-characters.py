class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for w in words:
            word_count = Counter(w)
            if all(word_count[c] <= char_count[c] for c in word_count):
                total += len(w)

        return total