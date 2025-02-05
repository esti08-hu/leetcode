class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        key_value_pairs = {}
        for i in range(len(s)):
            key_value_pairs[indices[i]] = s[i]

        sorted_char = [key_value_pairs[i] for i in sorted(key_value_pairs)]
        return "".join(sorted_char)
