class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]
        self.size = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.pre = [1]
            self.size = 0
        else:
            self.pre.append(self.pre[-1]*num)
            self.size+=1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0

        l = self.size - k
        r = self.size

        return self.pre[r] // self.pre[l]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)