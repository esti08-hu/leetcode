class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_val_set = set(Counter(s).values())

        if len(s_val_set) != 1:
            return False
        else:
            return True
