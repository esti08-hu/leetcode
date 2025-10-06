class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = defaultdict(int)
        for num in arr:
            rem = num % k
            count[rem] += 1
        for r in range(k):
            if r == 0:
                if count[r] % 2 != 0:
                    return False
            elif 2*r == k:
                if count[r] % 2 != 0:
                    return False
            else:
                if count[r] != count[k - r]:
                    return False
        return True
        