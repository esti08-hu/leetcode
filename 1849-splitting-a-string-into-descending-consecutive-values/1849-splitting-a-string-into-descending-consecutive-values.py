class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start: int, prev: int) -> bool:
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                curr = int(s[start:end])
                if curr + 1 == prev:
                    if backtrack(end, curr):
                        return True
                elif curr >= prev:
                    break

            return False

        for end in range(1, len(s)):
            first_num = int(s[:end])
            if backtrack(end, first_num):
                return True

        return False