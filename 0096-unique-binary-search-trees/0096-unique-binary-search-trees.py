class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)

        def count(nodes):
            if nodes <= 1:
                return 1
            
            ways = 0

            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root

                ways += count(left) * count(right)
            return ways

        return count(n)