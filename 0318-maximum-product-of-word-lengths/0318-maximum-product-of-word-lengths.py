class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_dict = {}
        for word in words:
            word_dict[word] = set(word)

        max_prod = 0

        for i in range(len(words)-1):
            curr = word_dict[words[i]]
            for j in range(i+1, len(words)):
                for c in curr:
                    if c in word_dict[words[j]]:
                        break
                else:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))

        return max_prod
        