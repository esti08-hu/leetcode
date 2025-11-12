class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        p = n // 2
        if n % 2:
            return pow(5, p + 1, MOD) * pow(4, p, MOD) % MOD
        return pow(5, p, MOD) * pow(4, p, MOD) % MOD