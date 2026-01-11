class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
            
        first_cap = True if word[0].isupper() else False
        second_cap = True if word[1].isupper() else False

        if not first_cap and second_cap:
            return False

        if first_cap and second_cap:
            for i in range(2, len(word)):
                if word[i].islower():
                    return False
        if first_cap and not second_cap:
            for i in range(2, len(word)):
                if word[i].isupper():
                    return False
        if not first_cap and not second_cap:
            for i in range(2, len(word)):
                if word[i].isupper():
                    return False
        
        return True