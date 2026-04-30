class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}
        
        def is_sorted(word1, word2):
            min_len = min(len(word1), len(word2))
            
            for i in range(min_len):
                char1 = word1[i]
                char2 = word2[i]
                
                if char1 != char2:
                    return order_map[char1] < order_map[char2]

            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i+1]):
                return False
                
        return True