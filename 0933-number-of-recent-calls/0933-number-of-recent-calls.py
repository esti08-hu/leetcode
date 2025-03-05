from queue import Queue

class RecentCounter:

    def __init__(self):
        self.Q = Queue()

    def ping(self, t: int) -> int:
        self.Q.put(t)  
        
        while not self.Q.empty() and self.Q.queue[0] < t - 3000:
            self.Q.get()  
            
        return self.Q.qsize()

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)