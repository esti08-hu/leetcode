class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = Counter((x % k) for x in arr)
        if cnt[0] % 2 != 0:
            return False

        if k % 2 == 0 and cnt[k // 2] % 2 != 0:
            return False

        for r in range(1, (k + 1) // 2):
            if cnt[r] != cnt[k - r]:
                return False

        return True
