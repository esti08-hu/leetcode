class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class FrontMiddleBackQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get_middle(self):
        if self.size == 0:
            return None
            
        mid = (self.size - 1) // 2
        
        curr = self.head
        for _ in range(mid):
            curr = curr.next
        
        return curr

    def pushFront(self, val: int) -> None:
        new_node = Node(val)
        
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def pushMiddle(self, val: int) -> None:
        if self.size == 0:
            self.pushFront(val)
            return
            
        if self.size == 1:
            new_node = Node(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return
        
        mid = self.size // 2
        if self.size % 2 == 1:
            mid = (self.size - 1) // 2
        
        curr = self.head
        for _ in range(mid):
            curr = curr.next
        
        new_node = Node(val)
        new_node.prev = curr.prev
        new_node.next = curr
        
        if curr.prev:
            curr.prev.next = new_node
        else:
            self.head = new_node
            
        curr.prev = new_node
        self.size += 1

    def pushBack(self, val: int) -> None:
        new_node = Node(val)
        
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        
        val = self.head.val
        
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return val

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
            
        if self.size == 1:
            return self.popFront()
            
        mid = self.get_middle()
        val = mid.val
        
        if mid.prev:
            mid.prev.next = mid.next
        else:
            self.head = mid.next
            
        if mid.next:
            mid.next.prev = mid.prev
        else:
            self.tail = mid.prev
            
        self.size -= 1
        return val

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        
        val = self.tail.val
        
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return val
