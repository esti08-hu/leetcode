class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) ^ set(word2) != set():
            return False
        s_w1 = sorted(word1)
        s_w2 = sorted(word2)
        d_w1 = set(s_w1)
        d_w2 = set(s_w2)
        c_w1 = []
        c_w2 =[]

        for i in d_w1:
            c_w1.append(s_w1.count(i))

        for j in d_w2:
            c_w2.append(s_w2.count(j))
            

        return sorted(c_w1) == sorted(c_w2)