class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_valid_sum(s, target):

            def dfs(idx, curr_sum):
                if idx == len(s):
                    return curr_sum == target
                for i in range(idx + 1, len(s) + 1):
                    if dfs(i, curr_sum + int(s[idx:i])):
                        return True
                return False

            return dfs(0, 0)

        total = 0
        for i in range(1, n + 1):
            square = i * i
            if is_valid_sum(str(square), i):
                total += square

        return total