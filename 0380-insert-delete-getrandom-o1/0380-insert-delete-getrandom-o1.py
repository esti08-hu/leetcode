class RandomizedSet:
    def __init__(self):
        self.numbers = {} 
        self.values = []
        
    def insert(self, val: int) -> bool:
        if val in self.numbers:
            return False
        self.numbers[val] = len(self.values)
        self.values.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.numbers:
            return False
        index = self.numbers[val]
        last_val = self.values[-1]
        self.values[index] = last_val  
        self.numbers[last_val] = index
        self.values.pop()
        del self.numbers[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)