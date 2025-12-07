class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(mid):
            total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            return total >= n

        def lcm(x, y):
            return x * y // math.gcd(x, y)
        
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)

        l, r = 1, 2 * 10**9
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


