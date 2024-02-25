from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        maxElement = max(nums)
        if min(nums) == 1:
            return False

        parent = list(range(maxElement + 1))
        rank = [1] * (maxElement + 1)

        def find(a: int) -> int:
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        def union(a: int, b: int) -> None:
            a = find(a)
            b = find(b)
            if a == b:
                return
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            rank[a] += rank[b]

        for num in nums:
            x = num
            while x > 1:
                p = 2
                while p * p <= x:
                    if x % p == 0:
                        union(p, num)
                        while x % p == 0:
                            x = x // p
                    p += 1
                if x > 1:
                    union(x, num)
                    x = 1

        p = find(nums[0])
        return all(find(num) == p for num in nums)