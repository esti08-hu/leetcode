class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        if len(self.max_heap) == 0 or -self.max_heap[0] > num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        

        if len(self.min_heap)+1 < len(self.max_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) /2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()