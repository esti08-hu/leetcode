class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        s_count = Counter(s)

        len_1 = s_count['1']
        len_0 = s_count['0']
        s1= ''
        if len_1 > 1:
            for i in range(len_1-1):
                s1+="1"
        if len_0 > 0:
            for i in range(len_0):
                s1+="0"
        if len_1 > 0:
            s1+="1"
        return s1
