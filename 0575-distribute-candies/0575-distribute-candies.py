class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        type_num = len(set(candyType))

        n = len(candyType) // 2

        return min(n, type_num)

