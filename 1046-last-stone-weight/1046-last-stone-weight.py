class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] = -stones[i]
        heapify(stones)

        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)

            left_over = abs(stone1-stone2)
            if left_over == 0:
                continue
            heappush(stones, -left_over)
        if stones: return -stones[0]
        return 0
