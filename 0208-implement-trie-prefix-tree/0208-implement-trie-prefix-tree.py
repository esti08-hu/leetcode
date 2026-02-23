class TrieNode():
    def __init__(self):
        self.node = [0] * 26
        self.isEnd = False
class Trie:
    def convert(slef, ch):
        return ord(ch)-ord('a')

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            idx = self.convert(word[i])
            if not curr.node[idx]:
                new_node = TrieNode()
                curr.node[idx] = new_node
            curr = curr.node[idx]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            idx = self.convert(word[i])
            if not curr.node[idx]:
                return False
            curr = curr.node[idx]
        
        return curr.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            idx = self.convert(prefix[i])
            if not curr.node[idx]:
                return False
            curr = curr.node[idx]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)