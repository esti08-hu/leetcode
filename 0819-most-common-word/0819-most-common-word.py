class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.split(r'[^a-zA-Z]+', paragraph.lower())
        
        word_counter = Counter(w for w in words if w and w not in banned_set)
        
        return word_counter.most_common(1)[0][0]