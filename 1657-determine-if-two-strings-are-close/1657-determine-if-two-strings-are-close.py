class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
            
        w1_cnt = Counter(word1)
        w2_cnt = Counter(word2)

        w1_cnt_lst = sorted(list(w1_cnt.values()))
        w2_cnt_lst = sorted(list(w2_cnt.values()))

        return True if w1_cnt_lst == w2_cnt_lst else False
