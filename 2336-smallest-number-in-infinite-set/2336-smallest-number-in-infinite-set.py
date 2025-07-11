class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.num_set = set()
        

    def popSmallest(self) -> int:
        if self.num_set:
            smallest = min(self.num_set)
            self.num_set.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.num_set:
            self.num_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)