class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1] + [0] * (n - 1)
        idx = [0] * k

        for i in range(1, n):
            candidates = []
            for j in range(k):
                candidates.append(primes[j] * ugly[idx[j]])
            nxt_num = min(candidates)
            ugly[i] = nxt_num

            for j in range(k):
                if candidates[j] == nxt_num:
                    idx[j] += 1
        return ugly[-1]