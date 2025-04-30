class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums
        heapify(heap)
        
        count = 0
        while len(heap) >= 2 :
            x, y = heappop(heap), heappop(heap)
            if x >= k and y >= k:
                return count

            else:
                heappush(heap, (min(x, y) * 2 + max(x, y)))
                count += 1
        
        return count 

