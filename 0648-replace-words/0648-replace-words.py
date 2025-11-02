class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        for word in set(dictionary):
            curr  = self.root
            for c in word:
                idx = ord(c) - ord("a")
                if not curr.children[idx]:
                    curr.children[idx] = Trie()
                curr = curr.children[idx]
            curr.isEnd = True

        words = sentence.split(" ")
        for i, word in enumerate(words):
            curr = self.root
            track = ""

            for c in word:
                idx = ord(c) - ord("a")

                if curr.children[idx] is None:
                    break
                track += c
                curr = curr.children[idx]

                if curr.isEnd:
                    words[i] = track
                    break
                
        return " ".join(map(str, words))
            
