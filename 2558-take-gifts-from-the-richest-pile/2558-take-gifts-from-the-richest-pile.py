import math
from typing import List
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-x for x in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            new_val = int(math.sqrt(largest))
            heapq.heappush(max_heap, -new_val)
        
        return sum(-x for x in max_heap)