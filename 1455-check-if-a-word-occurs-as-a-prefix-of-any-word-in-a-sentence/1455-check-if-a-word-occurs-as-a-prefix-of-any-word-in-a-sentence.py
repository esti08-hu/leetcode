class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split(" ")
        n = len(searchWord)
        for i in range(len(sentence_list)):
            if searchWord == sentence_list[i][:n]:
                return i+1
        
        return -1
            