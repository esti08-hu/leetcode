class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        word_substring = set()

        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                word_substring.add(word[i:j])
        
        count = 0
        for pattern in patterns:
            if pattern in word_substring:
                count += 1
        
        return count