class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        if sum(candies) < k:
            return 0
        elif sum(candies) == k:
            return 1
             
        left, right = 1, max(candies)

        def check(mid):
            _sum = 0
            for c in candies:
                _sum += (c // mid)

            return _sum >= k

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right