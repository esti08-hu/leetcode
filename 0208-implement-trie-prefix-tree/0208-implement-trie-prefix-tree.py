class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            c_idx = ord(c) - ord("a")
            if curr.children[c_idx] is None:
                curr.children[c_idx] = TrieNode()
            curr = curr.children[c_idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            c_idx = ord(c) - ord("a")
            if curr.children[c_idx] is None:
                return False
            curr = curr.children[c_idx]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            c_idx = ord(c) - ord("a")
            if curr.children[c_idx] is None:
                return False
            curr = curr.children[c_idx]
        return True
 
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)