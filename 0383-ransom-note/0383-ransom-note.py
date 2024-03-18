class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
            
        for char in ransomNote:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False
        
        return True