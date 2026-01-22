class MyHashSet:

    def __init__(self):
        self.hashSet = [0] * (10**6 + 1)

    def add(self, key: int) -> None:
        if not self.hashSet[key]:
            self.hashSet[key] = key
        
    def remove(self, key: int) -> None:
        if self.hashSet[key]:
            self.hashSet[key] = 0

    def contains(self, key: int) -> bool:
        return self.hashSet[key] != 0

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)