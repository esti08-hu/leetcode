class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = Node(homepage)
        self.curr = self.tab

    def visit(self, url: str) -> None:
        url_node = Node(url)
        self.curr.next = url_node
        url_node.prev = self.curr
        self.curr = url_node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)