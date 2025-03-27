from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, max(candies)

        def check(mid):
            _sum = 0
            for c in candies:
                _sum += (c // mid)
                # print(_sum)
            return _sum >= k

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right