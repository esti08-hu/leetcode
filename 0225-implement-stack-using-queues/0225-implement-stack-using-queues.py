from queue import Queue

class MyStack:

    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def push(self, x: int) -> None:
        self.Q2.put(x)
        while not self.Q1.empty():
            self.Q2.put(self.Q1.get())
        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self) -> int:
        if self.Q1.empty():
            return None
        return self.Q1.get()

    def top(self) -> int:
        if self.Q1.empty():
            return None
        top_element = self.Q1.get()
        self.Q2.put(top_element)
        while not self.Q1.empty():
            self.Q2.put(self.Q1.get())
        self.Q1, self.Q2 = self.Q2, self.Q1
        return top_element

    def empty(self) -> bool:
        return self.Q1.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.get()
# param_3 = obj.top()
# param_4 = obj.empty()