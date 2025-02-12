class RandomizedSet:
    def __init__(self):
        self.numbers = {}  # dictionary to store values and their indices
        self.values = []  # list to store values
        
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
        self.values[index] = last_val  # move last value to the removed value's position
        self.numbers[last_val] = index  # update the index of the last value in the dictionary
        self.values.pop()  # remove the last value from the list
        del self.numbers[val]  # remove the value from the dictionary
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)