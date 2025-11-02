class Trie:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - ord("a")

            if not curr.children[idx]:
                curr.children[idx] = Trie()
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if not node:
                return False
                
            if idx == len(word):
                return node.isEnd
            
            char = word[idx]
            if char == ".":
                for child in node.children:
                    if child and dfs(child, idx+1):
                        return True
                return False
            else:
                ci = ord(char) - ord("a")
                if ci < 0 or ci >= 26:
                    return False
                child = node.children[ci]
                return dfs(child, idx + 1)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)