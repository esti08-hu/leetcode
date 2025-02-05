from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        summ = 0

        for word in words:
            word_count = Counter(word)
            if word_count <= chars_count:
                summ += len(word)

        return summ