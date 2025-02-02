class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = list(s.split())
        l_word = max(s_list, key=len)
        res=[]
        for i in range(len(l_word)):
            var = ""
            for w in s_list:
                if i < len(w):
                    var+=w[i]
                else:
                    var+=" "
            res.append(var.rstrip())
        return res

        