class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set()
        for c in allowed:
            allowed_set.add(c)

        count = 0
        for word in words:
            for c in word:
                if c not in allowed_set:
                    break
            else:
                count += 1

        return count