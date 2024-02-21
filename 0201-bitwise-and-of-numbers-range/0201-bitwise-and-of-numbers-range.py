class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        # Left shift the common prefix to obtain the result
        return left << shift