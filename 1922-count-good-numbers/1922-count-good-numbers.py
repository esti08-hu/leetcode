class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        p = n // 2
        def mod_pow(a, b, mod):
            if b == 0:
                return 1
            half = mod_pow(a, b // 2, mod)
            if b % 2 == 0:
                return (half * half) % mod
            else:
                return (half * half * a) % mod
                
        if n % 2:
            return mod_pow(5, p + 1, MOD) * mod_pow(4, p, MOD) % MOD
        return mod_pow(5, p, MOD) * mod_pow(4, p, MOD) % MOD