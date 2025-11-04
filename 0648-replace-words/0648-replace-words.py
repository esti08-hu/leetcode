class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        for word in set(dictionary):
            curr  = self.root
            for c in word:
                if not curr.children[c]:
                    curr.children[c] = Trie()
                curr = curr.children[c]
            curr.isEnd = True

        words = sentence.split(" ")
        for i, word in enumerate(words):
            curr = self.root
            track = ""

            for c in word:
                if curr.children[c] is None:
                    break
                track += c
                curr = curr.children[c]

                if curr.isEnd:
                    words[i] = track
                    break

        return " ".join(map(str, words))
