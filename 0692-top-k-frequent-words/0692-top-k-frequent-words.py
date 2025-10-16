class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)

        sorted_words = sorted(words_count.keys(), key=lambda w: (-words_count[w], w))

        return sorted_words[:k]