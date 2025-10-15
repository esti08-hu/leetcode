class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if idx not in curr:
                curr[idx] = {}
            curr = curr[idx]
        curr['*'] = ''
        

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if idx not in curr:
                return False
            curr = curr[idx]
        return "*" in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord("a")
            if idx not in curr:
                return False
            curr = curr[idx]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)