class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = 0
        odd_count = 0
        
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return min(even_count, odd_count)