class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd
            
            char = word[idx]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, idx+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], idx+1)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)