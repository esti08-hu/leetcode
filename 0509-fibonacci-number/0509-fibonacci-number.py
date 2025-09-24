class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def dfs(x):
            if x == 0:
                return 0
            if x == 1:
                return 1

            if x in cache:
                return cache[x]
            cache[x] = self.fib(x-2) + self.fib(x-1)
            return cache[x]

        return dfs(n)
