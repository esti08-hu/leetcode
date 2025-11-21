class Solution:
    def minimumPushes(self, word: str) -> int:
        """

        x y c d e f g h i h s

        if word len <= 8 return len the word

        the first 8 chars are pushed 1x the next 8 chars should be pushed 2x if their is not duplicate
        what if duplicate
        may be 1x or 2x for the second 8 charactors. 
                                                1ft 8c 
        dic = {x:1, y:1, c:1, d:1, e:1, f:1, g:1, h:1, i:2, }
        len(dic) 9 // 8 => math.ciel (1.afda)
        """
        push_map = defaultdict(int)
        res = 0
        for c in word:
            if c not in push_map:
                if not push_map:
                    push_map[c] = 1
                else:
                    push_map[c] = 1+len(push_map)//8
                res+=push_map[c]
            else:
                res+=push_map[c]
        print(push_map)
        return res
