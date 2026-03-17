class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a_sum = sum(aliceSizes)
        b_sum = sum(bobSizes)
        bob_set = set(bobSizes)
        
        for a in aliceSizes:
            # y = x + (SumB - SumA) / 2
            needed = a + (b_sum - a_sum) // 2
            if needed in bob_set:
                return [a, needed]