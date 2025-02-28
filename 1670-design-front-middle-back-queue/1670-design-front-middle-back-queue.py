class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def pushFront(self, val: int) -> None:
                # create a node
        new_node = Node(val)

        #check head 
        if not self.head:
            self.head = self.tail = new_node
        else:        
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pushMiddle(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
            self.size+=1
            return 
        
        mid = self.size // 2

        curr = self.head
        for _ in range(mid):
            curr = curr.next

        new_node.prev = curr.prev
        new_node.next = curr

        if curr.prev:
            curr.prev.next = new_node
        curr.prev = new_node

        if curr == self.head:
            self.head = new_node
        
        self.size += 1  

    def pushBack(self, val: int) -> None:
        new_node = Node(val)

        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def popFront(self) -> int:
        if not self.head:
            return -1

        val = self.head.val
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail =  None
        self.size -= 1

        return val

    def popMiddle(self) -> int:
        if not self.head:
            return -1
        mid = (self.size - 1)//2

        curr = self.head

        for _ in range(mid):
            curr = curr.next
            
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next
        if curr == self.tail:
            self.tail = curr.prev

        if self.size == 1:
            self.head = self.tail = None

        self.size -= 1

        return curr.val

    def popBack(self) -> int:
        if not self.tail:
            return -1
        
        val = self.tail.val
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self.size -= 1

        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()